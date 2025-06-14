async function fetchWithREST() {
    const response = await fetch("http://localhost:8000/readings");
    const data = await response.json();
  
    const labels = data.map(reading => new Date(reading.timestamp).toLocaleTimeString());
    const temps = data.map(reading => reading.temperature);
  
    const ctx = document.getElementById('readingChart').getContext('2d');
  
    let chartInstance = null;

async function fetchWithREST() {
  const response = await fetch("http://localhost:8000/readings");
  const data = await response.json();

  const labels = data.map(reading => new Date(reading.timestamp).toLocaleTimeString());
  const temps = data.map(reading => reading.temperature);

  const ctx = document.getElementById('readingChart').getContext('2d');

    // 💥 Destroy old chart if it exists
    if (chartInstance !== null) {
        chartInstance.destroy();
    }

    chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
        labels: labels,
        datasets: [{
            label: 'Temperature (°C)',
            data: temps,
            fill: false,
            borderColor: 'blue',
            tension: 0.1
        }]
        }
    });
    }

    new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [{
          label: 'Temperature (°C)',
          data: temps,
          fill: false,
          borderColor: 'blue',
          tension: 0.1
        }]
      }
    });
  }
  