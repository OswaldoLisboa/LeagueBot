template = """<meta charset="UTF-8">
<body>
{body}
</body>

<style>
    table {{
        color: 	333;
        font-family: Helvetica;
        width: 100%;
        border-collapse:
        collapse;
        border-spacing: 0;
    }}
    td, th {{
        border: 1px solid transparent; /* No more visible border */
        height: 40px;
        width: 100px;
    }}
    th {{
        background: #1d976c; /* Darken header a bit */
        font-weight: bold;
        text-align: center;
        color: 	#FFFAFA;
    }}
    td {{
        background: #63da91;
        text-align: center;
    }}
    table tr:nth-child(odd) td{{
      background-color: #63fa91;
    }}
    .team {{
      width: 30%;
    }}
</style>"""
