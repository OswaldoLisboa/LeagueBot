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

  <h1>Relegated to {division}</h1>

  <table>
    <tr>
      <td><img src="{relegated1_crest_file}.png" alt="{relegated1_name}"></td>
      <td><img src="{relegated2_crest_file}.png" alt="{relegated2_name}"></td>
      <td><img src="{relegated3_crest_file}.png" alt="{relegated3_name}"></td>
    </tr>
    <tr>
      <td class="team">{relegated1_name}</td>
      <td class="team">{relegated2_name}</td>
      <td class="team">{relegated3_name}</td>
    </tr>
    <tr>
      <td class="team">{relegated1_twitter}</td>
      <td class="team">{relegated2_twitter}</td>
      <td class="team">{relegated3_twitter}</td>
    </tr>
  </table>

</body>
"""
