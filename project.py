import requests
import streamlit as st
import re

def main():
    st.set_page_config(layout='wide')

    page_title = st.title("The Web Cookbook")
    query = st.text_input("Search for a recipe")

    col1, col2 = st.columns(2)

    with col1:
        intolerances = st.multiselect("Intolerances", [
            "Dairy",
            "Egg",
            "Gluten",
            "Grain",
            "Peanut",
            "Seafood",
            "Sesame",
            "Soy",
            "Wheat"
        ])

    with col2:
        diet = st.selectbox("Diet", [
            "No Specific Diet",
            "Gluten Free",
            "Ketogenic",
            "Vegetarian",
            "Lacto-Vegetarian",
            "Ovo-Vegetarian",
            "Vegan",
            "Pescetarian",
            "Paleo",
            "Primal",
            "Low FODMAP",
            "Whole30"
        ])

    data = None

    if query:
        try:
            data = get_recipe(query=query, diet=diet, intolerances=intolerances)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        pass

    # Display retrieved data if available
    if data and "results" in data:
        recipes = data["results"][:9]

    # Create columns to display data
        cols = st.columns(3)
        col3, col4 = st.columns(2)

        for _, recipe in enumerate(recipes):
            title = recipe["title"]
            cut_title = recipe["title"][:32] + "..." if len(recipe["title"]) > 32 else recipe["title"]
            recipe_id = recipe["id"]

            with cols[_ % 3]:
                st.image(recipe["image"])
                st.text(cut_title)
                if st.button(label="View Ingredients" + " "*_):
                    ingredients = get_ingredients(recipe_id)
                    instructions = get_instructions(recipe_id)

                    with col3: # Ingredients
                        st.subheader(f"Ingredients for {title}")
                        for __, ingredient in enumerate(ingredients["ingredients"]):
                            name = ingredient["name"]
                            amount = ingredient["amount"]["metric"]["value"]
                            unit = ingredient["amount"]["metric"]["unit"]
                            __ += 1
                            st.markdown(f"**{__}**. **{name}** - {amount}{unit.lower()}")

                    with col4: # Instructions
                        st.subheader(f"Instructions for {title}")
                        instructions = instructions[0]["steps"]
                        for step in instructions:
                            number = step["number"]
                            description = re.sub(r'\.(?!\s|$)', '. ', step["step"]) #Regular expression to format the description
                            st.markdown(f"**{number}**. {description}")


def get_recipe(query="", cuisine="", diet="", type="", intolerances="", number=9):
    key = "4f088b97d9a3497a83eecf3e6f984805"
    URL = "https://api.spoonacular.com/recipes/complexSearch"

    if diet == "No Specific Diet":
        diet = ""

    params = {
        "cuisine": cuisine.title(),
        "diet": diet,
        "type": type,
        "intolerances": intolerances,
        "number": number,
        "query": query,
        "apiKey": key
    }

    try:
        response = requests.get(URL, params=params)
        return response.json()

    except requests.RequestException as e:
        return f"Request failed: {str(e)}"


def get_ingredients(recipe_id, system="metric"):
    key = "4f088b97d9a3497a83eecf3e6f984805"
    URL = f"https://api.spoonacular.com/recipes/{recipe_id}/ingredientWidget.json"

    params = {"apiKey": key}

    try:
        response = requests.get(URL, params=params)
        return response.json()

    except requests.RequestException as e:
        return f"Request failed: {str(e)}"


def get_instructions(recipe_id):
    key = "4f088b97d9a3497a83eecf3e6f984805"
    URL = f"https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions"

    params = {"id": int(recipe_id), "apiKey": key}

    try:
        response = requests.get(URL, params=params)
        return response.json()

    except requests.RequestException as e:
        return f"Request failed: {str(e)}"


#def substitute(ingredient):
    key = "4f088b97d9a3497a83eecf3e6f984805"
    URL = "https://api.spoonacular.com/food/ingredients/substitutes"

    params = {"ingredientName": ingredient.lower(), "apiKey": key}

    try:
        response = requests.get(URL, params=params)
        response = response.json()
        return response["substitutes"]

    except requests.RequestException as e:
        return f"Request failed: {str(e)}"


if __name__ == "__main__":
    main()


#4f088b97d9a3497a83eecf3e6f984805 - Aymen
#9815d21b945e4546bc171dba4b266adb - NizarAlt
#c90b4f27ba294c868fc10585d175526d - Uniflare
#1923d24e46514b2b802f73f6e41626f4 - Original
