from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def find_right_car(vehicle_type, budget, fuel_efficiency, terrain_type, num_seats):
    llm = OpenAI(temperature=0.7)
    prompt_template = PromptTemplate(
        input_variables=['vehicle_type', 'budget', 'fuel_efficiency', 'terrain_type', 'num_seats'],
        template="Recommend a {vehicle_type} within a {budget} budget pkr that is {fuel_efficiency} on fuel, suitable for {terrain_type} terrain, and has {num_seats} seats."
    )

    car_chain = LLMChain(llm=llm, prompt=prompt_template)
    response = car_chain({
        'vehicle_type': vehicle_type,
        'budget': budget,
        'fuel_efficiency': fuel_efficiency,
        'terrain_type': terrain_type,
        'num_seats': num_seats
    })
    return response

def main():
    st.title("Find yourself a right car")
    st.text("Recommended Car: ")

    # Collect user input
    vehicle_type = st.sidebar.selectbox("Select Vehicle Type", ["Sedan", "SUV", "Truck"])
    budget = st.sidebar.text_input("Enter Budget (in pkr):")
    fuel_efficiency = st.sidebar.selectbox("Select Fuel Efficiency", ["Fuel-Efficient", "Standard", "Not Fuel-Efficient"])
    terrain_type = st.sidebar.selectbox("Select Terrain Type", ["City", "Off-Road", "Mixed"])
    num_seats = st.sidebar.number_input("Enter Number of Seats", min_value=1, max_value=10, value=5, step=1)

    # Generate recommendation
    if st.sidebar.button("Generate Recommendation"):
        response = find_right_car(vehicle_type, budget, fuel_efficiency, terrain_type, num_seats)
        st.success(response['text'])

if __name__ == "__main__":
    main()