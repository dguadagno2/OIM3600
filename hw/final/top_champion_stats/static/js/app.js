document.getElementById("puuid-form").addEventListener("submit", function(event) {
    event.preventDefault();
  
    // loading message 
    document.getElementById("loading").classList.remove("hidden");
    document.getElementById("error-message").classList.add("hidden");
  
    const puuid = document.getElementById("puuid-input").value.trim();
  
    // Fetch top champion data
    fetchTopChampions(puuid);
  });
  
  function fetchTopChampions(puuid) {
    fetch(`/api/get-top-champions?puuid=${puuid}`)
      .then(response => response.json())
      .then(data => {
        document.getElementById("loading").classList.add("hidden");
  
        if (data.error) {
          document.getElementById("error-message").classList.remove("hidden");
          return;
        }
  
        // Process and display the data for 50 and 20 games
        displayTopChampions(data.topChampions);
      })
      .catch(() => {
        document.getElementById("loading").classList.add("hidden");
        document.getElementById("error-message").classList.remove("hidden");
      });
  }
  
  function displayTopChampions(topChampions) {
    // Display the data for the last 50 games
    displayTable("table-50", topChampions[50]);
  
    // Display the data for the last 20 games
    displayTable("table-20", topChampions[20]);
  }
  
  // Used ChatGPT to debug dispay table, https://chatgpt.com/share/674fcf11-c128-8011-8cf4-d9863fc4dd5a 
  function displayTable(tableId, champions) {
    const tableBody = document.getElementById(tableId).getElementsByTagName("tbody")[0];
    tableBody.innerHTML = ''; // Clear previous results
    
    champions.forEach((champion, index) => {
      const row = tableBody.insertRow();
      
      row.innerHTML = `
        <td>${index + 1}</td>
        <td>${champion.champion}</td>
        <td>${champion.avg_kda.toFixed(2)}</td>
        <td>${(champion.win_rate * 100).toFixed(2)}%</td>
        <td>${champion.games_played}</td>
      `;
    });
  }
  