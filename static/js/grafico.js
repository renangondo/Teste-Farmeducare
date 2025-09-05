document.addEventListener('DOMContentLoaded', function() {
    // Verificar se os elementos dos gráficos existem na página
    const lineChart = document.getElementById('lineChart');
    const pieChart = document.getElementById('pieChart');
    
    // Verificar se os dados foram passados do Django
    const hasDjangoData = typeof window.graficoData !== 'undefined';
    
    // Dados (usar dados do Django se disponíveis, caso contrário dados de exemplo)
    const meses = hasDjangoData ? window.graficoData.meses : ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'];
    const receitas = hasDjangoData ? window.graficoData.receitas : [12000, 19000, 15000, 18000, 22000, 25420];
    const despesas = hasDjangoData ? window.graficoData.despesas : [8000, 12000, 10000, 11000, 15000, 16800];
    
    const categorias = hasDjangoData ? window.graficoData.categorias : ['Insumos', 'Manutenção', 'Salários', 'Medicamentos', 'Outros'];
    const valores = hasDjangoData ? window.graficoData.valores : [12000, 8000, 15000, 5000, 4000];
    
    // Formatar meses para exibição mais amigável
    const mesesFormatados = meses.map(mes => {
        const [ano, mesNum] = mes.split('-');
        const mesesPtBr = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'];
        return `${mesesPtBr[parseInt(mesNum) - 1]}/${ano.substring(2)}`;
    });
    
    // Gráfico de Linhas - Receitas vs Despesas
    if (lineChart) {
        const lineCtx = lineChart.getContext('2d');
        
        new Chart(lineCtx, {
            type: 'line',
            data: {
                labels: mesesFormatados,
                datasets: [
                    {
                        label: 'Receitas',
                        data: receitas,
                        borderColor: 'rgb(75, 192, 192)',
                        backgroundColor: 'rgba(75, 192, 192, 0.1)',
                        tension: 0.1,
                        fill: true
                    },
                    {
                        label: 'Despesas',
                        data: despesas,
                        borderColor: 'rgb(255, 99, 132)',
                        backgroundColor: 'rgba(255, 99, 132, 0.1)',
                        tension: 0.1,
                        fill: true
                    }
                ]
            },
            options: {
                responsive: true,
                plugins: {
                    title: {
                        display: true,
                        text: 'Evolução Mensal'
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const label = context.dataset.label || '';
                                const value = context.raw || 0;
                                return `${label}: R$ ${value.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`;
                            }
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: function(value) {
                                return 'R$ ' + value.toLocaleString('pt-BR');
                            }
                        }
                    }
                }
            }
        });
    }
    
    // Gráfico de Pizza - Distribuição de Despesas
    if (pieChart) {
        const pieCtx = pieChart.getContext('2d');
        
        new Chart(pieCtx, {
            type: 'pie',
            data: {
                labels: categorias,
                datasets: [{
                    data: valores,
                    backgroundColor: [
                        'rgb(255, 99, 132)',
                        'rgb(54, 162, 235)',
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',
                        'rgb(153, 102, 255)',
                        'rgb(255, 159, 64)',
                        'rgb(201, 203, 207)'
                    ],
                    hoverOffset: 4
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'right',
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const label = context.label || '';
                                const value = context.raw || 0;
                                const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                const percentage = Math.round((value / total) * 100);
                                return `${label}: R$ ${value.toLocaleString('pt-BR', {minimumFractionDigits: 2})} (${percentage}%)`;
                            }
                        }
                    }
                }
            }
        });
    }
    
    // Atualizar cards com dados reais se disponíveis
    if (hasDjangoData && window.graficoData.totais) {
        updateSummaryCards(window.graficoData.totais);
    }
});

// Função para atualizar os cards de resumo com dados reais
function updateSummaryCards(totais) {
    // Atualizar card de receitas
    const receitaCard = document.querySelector('.card-receita .card-info p');
    if (receitaCard && totais.receitas !== undefined) {
        receitaCard.textContent = `R$ ${totais.receitas.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`;
    }
    
    // Atualizar card de despesas
    const despesaCard = document.querySelector('.card-despesa .card-info p');
    if (despesaCard && totais.despesas !== undefined) {
        despesaCard.textContent = `R$ ${totais.despesas.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`;
    }
    
    // Atualizar card de saldo
    const saldoCard = document.querySelector('.card-saldo .card-info p');
    if (saldoCard && totais.saldo !== undefined) {
        saldoCard.textContent = `R$ ${totais.saldo.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`;
        if (totais.saldo < 0) {
            saldoCard.style.color = '#e74c3c';
        } else {
            saldoCard.style.color = '#2ecc71';
        }
    }
}

// Funções auxiliares para gráficos
function formatCurrency(value) {
    return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value);
}

function updateChartData(chart, newData) {
    chart.data.datasets[0].data = newData;
    chart.update();
}