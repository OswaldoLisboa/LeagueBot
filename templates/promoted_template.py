template = """<style>
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

  <h1>Promoted to {division}</h1>

  <table>
    <tr>
      <td><img src="{promoted1_crest_file}.png" alt="{promoted1_name}"></td>
      <td><img src="{promoted2_crest_file}.png" alt="{promoted2_name}"></td>
      <td><img src="{promoted3_crest_file}.png" alt="{promoted3_name}"></td>
    </tr>
    <tr>
      <td class="team">{promoted1_name}</td>
      <td class="team">{promoted2_name}</td>
      <td class="team">{promoted3_name}</td>
    </tr>
    <tr>
      <td class="team">{promoted1_twitter}</td>
      <td class="team">{promoted2_twitter}</td>
      <td class="team">{promoted3_twitter}</td>
    </tr>
  </table>

</body>
"""
