template = """<div class="container">
  <div></div>
  <div class="inside text">{division}</div>
  <div></div>
  <div class="inside text">Matchday {matchday}</div>
  <div></div>
  <div class="inside text">Game {game}</div>
  <div></div>
  <div></div>
  <div class="inside"><img class="crest" src="{home_crest}" alt="{home_name}"></div>
  <div class="inside score">{home_score}</div>
  <div class="inside score x">x</div>
  <div class="inside score">{away_score}</div>
  <div class="inside"><img class="crest" src="{away_crest}" alt="{away_name}"></div>
  <div></div>
  <div></div>
  <div class="inside text">{home_name}</div>
  <div></div>
  <div></div>
  <div></div>
  <div class="inside text">{away_name}</div>
  <div></div>
  <div></div>
  <div class="inside text">{home_twitter}</div>
  <div></div>
  <div></div>
  <div></div>
  <div class="inside text">{away_twitter}</div>
  <div></div>
</div>

<style media="screen">
  .container {{
    background-image: linear-gradient(to right, #1d976c, #63da91);
    height: 512px;
    width: 1024px;
    display: grid;
    grid-template-columns: 1fr 380px 2fr 140px 2fr 380px 1fr;
    grid-template-rows: 2fr 380px 1fr 1fr;
  }}

  .inside {{
    margin: auto;
  }}

  .crest {{
    width: 250px;
    height: auto;
  }}

  .text, .score {{
    color: 	#FFFAFA;
    font-family: helvetica;
  }}

  .text {{
    font-size: 22;
  }}

  .score {{
    font-size: 64;
  }}
</style>"""
