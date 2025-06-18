const ctx = document.getElementById('spendingChart').getContext('2d');
const spendingChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Other'],
        datasets: [{
            label: 'Monthly Spending',
            data: [500, 250, 150, 100, 200],
            backgroundColor: 'rgba(59, 130, 246, 0.6)',
            borderColor: 'rgba(59, 130, 246, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});