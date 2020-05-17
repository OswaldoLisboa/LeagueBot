template = """<meta charset="UTF-8">
<style>

  body {{
    background-image: -webkit-linear-gradient(right, #1d976c, #63da91);
    height: 512px;
    width: 1024px;
    color: 	#FFFAFA;
    font-family: helvetica;
    text-align: center;
  }}

  table {{
    border-spacing: 20;
    text-align: center;
    margin: auto;
  }}

  td, th {{
    border: 1px solid transparent;
    font-size: 32;
  }}

  img {{
    width: 250px;
    height: auto;
  }}

  .score {{
    font-size: 44;
  }}

  .team {{
    font-size: 32;
  }}

</style>
<body>

  <h1>{division} - Matchday {matchday} - Game {game}</h1>

  <table>
    <tr>
      <td><img src="{home_crest}.png" alt="{home_name}"></td>
      <td class="score">{home_score}</td>
      <td class="score">X</td>
      <td class="score">{away_score}</td>
      <td><img src="{away_crest}.png" alt="{away_name}"></td>
    </tr>
    <tr>
      <td class="team">{home_name}</td>
      <td></td>
      <td></td>
      <td></td>
      <td class="team">{away_name}</td>
    </tr>
    <tr>
      <td class="team">{home_twitter}</td>
      <td></td>
      <td></td>
      <td></td>
      <td class="team">{away_twitter}</td>
    </tr>
  </table>

</body>"""
