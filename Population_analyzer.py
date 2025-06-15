import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sub-question A 1)
def read_csv(filename):
    """Reads the CSV file and returns a DataFrame."""
    try:
        df = pd.read_csv(filename)
        return df[['city','country','population']]
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    pass

# Sub-question A 2)
def population_by_country(df):
    """Calculates the total population per country. Returns a dictionary where the keys
       will be the country names and the values will be their populations."""
    try:
        return df.groupby('country')['population'].sum().to_dict()
    except Exception as e:
        print(f"Error during calculation: {e}")
        return{}
    pass

# Sub-question A 3)
def largest_city_per_country(df):
    """Returns a dictionary where the keys
       will be the country names and the values will be tuples (city, population)
       with the largest city and its population for each country."""
    try:
        largest_cities = df.loc[df.groupby('country')['population'].idxmax()]
        return largest_cities.set_index('country')[['city', 'population']].to_dict('index')
    except Exception as e:
        print(f"Error during calculation: {e}")
        return {}
    #pass

# Sub-question A 4)
def total_population(df):
    """Calculates the total population of all cities and prints the result to the screen."""
    try:
        total = df['population'].sum()
        print(f"Total population: {total}")
    except Exception as e:
        print(f"Error during calculation: {e}")
    #pass

# Sub-question B 1)
def pie_chart_population(country_population):
    """Creates a pie chart for the population per country."""
    try:
         # Sort countries by population in descending order
        sorted_population = sorted(country_population.items(), key=lambda x: x[1], reverse=True)

        # Select the top 5 countries and group the rest
        top_5 = sorted_population[:5]
        rest = sum([x[1] for x in sorted_population[5:]])

        # Create labels that include the country name and population
        labels = [f"{x[0]} ({x[1]:,.0f})" for x in top_5] + [f"RestOfEurope ({rest:,.0f})"]

         # Create the sizes for the pie chart
        sizes = [x[1] for x in top_5] + [rest]

        # Create the pie chart
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("Population per country")
        plt.show()
    except Exception as e:
        print(f"Error creating pie chart: {e}")
    pass

# Sub-question B 2)
def bar_chart_largest_cities(df):
    """Creates a bar chart for the population of the largest cities."""
    try:
        largest_cities = largest_city_per_country(df)
        sorted_cities = sorted(largest_cities.items(), key=lambda x: x[1]['population'], reverse=True)
        countries = [x[0] for x in sorted_cities]
        populations = [x[1]['population'] for x in sorted_cities]
        plt.bar(countries, populations)
        plt.xticks(rotation=90)
        plt.title("Population of largest cities per country")
        plt.ylabel("Population")
        plt.show()
    except Exception as e:
        print(f"Error creating bar chart: {e}")
    pass

def main():
    """Main function of the program."""
    filename = r'd:\Program Files (x86)\VIsual-Studio_code\GitHub\EAP\PliPro\ERGASIA_4\ypoergasia_3\european_cities.csv'
    df = read_csv(filename)
    if df is None:
        return

    while True:
        print("\n=== Options Menu ===")
        print("1. Total population per country")
        print("2. Largest city per country")
        print("3. Total population")
        print("4. Population pie chart")
        print("5. Largest cities bar chart")
        print("6. Exit")

        try:
            choice = int(input("Select an action: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 1:
            country_population = population_by_country(df)
            if not country_population:
                print("No data available for total population per country.")
                continue
            print("Total population per country:")
            for country, population in country_population.items():
                print(f"{country}: {population}")

        elif choice == 2:
            largest_city = largest_city_per_country(df)
            if not largest_city:
                print("No data available for the largest city per country.")
                continue
            print("Largest city per country:")
            for country, v in largest_city.items():
                print(f"{country} ({v['city']}): {v['population']}")

        elif choice == 3:
            total_population(df)

        elif choice == 4:
            country_population = population_by_country(df)
            if not country_population:
                print("No data available to create the pie chart.")
                continue
            pie_chart_population(country_population)

        elif choice == 5:
            largest_cities = largest_city_per_country(df)
            if not largest_cities:
                print("No data available to create the bar chart.")
                continue
            bar_chart_largest_cities(df)

        elif choice == 6:
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
