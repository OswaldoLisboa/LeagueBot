template = """<div class="container">
  <div></div>
  <div class="inside text">Promoted to {division}</div>
  <div></div>
  <div class="inside"><img class="crest" src="{promoted1_crest_file}" alt="{promoted1_name}"></div>
  <div class="inside"><img class="crest" src="{promoted2_crest_file}" alt="{promoted2_name}"></div>
  <div class="inside"><img class="crest" src="Bpromoted3_crest_file" alt="{promoted3_name}"></div>
  <div class="inside text">{promoted1_name}</div>
  <div class="inside text">{promoted2_name}</div>
  <div class="inside text">{promoted3_name}</div>
  <div class="inside text">{promoted1_twitter}</div>
  <div class="inside text">{promoted2_twitter}</div>
  <div class="inside text">{promoted3_twitter}/div>
  <div></div>
</div>

<style media="screen">
  .container {{
    background-image: linear-gradient(to right, #1d976c, #63da91);
    height: 512px;
    width: 1024px;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
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
