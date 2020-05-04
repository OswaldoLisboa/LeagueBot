template = """<div class="container">
  <div class="inside text">{division} Champions</div>
  <div class="inside"><img class="crest" src="{crest_file}" alt="{champion_name}"></div>
  <div class="inside text">{champion_name}</div>
  <div class="inside text">{champion_twitter}</div>
  <div></div>
</div>

<style media="screen">
  .container {{
    background-image: linear-gradient(to right, #1d976c, #63da91);
    height: 512px;
    width: 1024px;
    display: grid;
    grid-template-rows: 1fr 380px 1fr 1fr;
  }}

  .inside {{
    margin: auto;
  }}

  .crest {{
    width: auto;
    height: 320px;
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
</style>
"""
