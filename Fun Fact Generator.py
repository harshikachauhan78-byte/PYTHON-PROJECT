import requests
from pywebio.output import put_html, put_text, put_buttons, clear, style
from pywebio.session import hold

def get_fun_fact(_):
    clear()

    put_html("""
    <h2>
        <img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png"
             width="50">
        Fun Fact Generator
    </h2>
    """)

    try:
        url = "https://uselessfacts.jsph.pl/random.json?language=en"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        fact = response.json()["text"]

        style(
            put_text(fact),
            "color: blue; font-size: 24px;"
        )

    except Exception as e:
        put_text(f"Error fetching fact: {e}")

    put_buttons(
        ["Get Another Fact"],
        onclick=get_fun_fact
    )

# Main page
put_html("""
<h2>
    <img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png"
         width="50">
    Fun Fact Generator
</h2>
""")

put_buttons(
    ["Generate Fun Fact"],
    onclick=get_fun_fact
)

hold()