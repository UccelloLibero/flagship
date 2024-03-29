from flask import Flask, render_template, request, jsonify, redirect, url_for
import random

app = Flask(__name__)

# Defining list of countries, their names and flags
countries = [
    {"name": "Afganistan", "flag": "static/Afganistan.png"},
    {"name": "Albania", "flag": "static/Albania.png" },
    {"name": "Algeria", "flag": "static/Algeria.png"},
    {"name": "Andora", "flag": "static/Andora.png"},
    {"name": "Angola", "flag": "static/Angola.png"},
    {"name": "Antigua and Barbuda", "flag": "static/Antigua and Barbuda.png"},
    {"name": "Argentina", "flag": "static/Argentina.png"},
    {"name": "Armenia", "flag": "static/Armenia.png"},
    {"name": "Aruba", "flag": "static/Aruba.png"},
    {"name": "Australia", "flag": "static/Australia.png"},
    {"name": "Austria", "flag": "static/Austria.png"},
    {"name": "Azerbaijan", "flag": "static/Azerbaijan.png"},
    {"name": "The Bahamas", "flag": "static/The Bahamas.png"},
    {"name": "Bahrain", "flag": "static/Bahrain.png"},
    {"name": "Bangladesh", "flag": "static/Bangladesh.png"},
    {"name": "Barbados", "flag": "static/Barbados.png"},
    {"name": "Belarus", "flag": "static/Belarus.png"},
    {"name": "Belgium", "flag": "static/Belgium.png"},
    {"name": "Belize", "flag": "static/Belize.png"},
    {"name": "Benin", "flag": "static/Benin.png"},
    {"name": "Bhutan", "flag": "static/Bhutan.png"},
    {"name": "Bolivia", "flag": "static/Bolivia.png"},
    {"name": "Bosnia and Herzegovina", "flag": "static/Bosnia and Herzegovina.png"},
    {"name": "Bonaire", "flag": "static/Bonaire.png"},
    {"name": "Botswana", "flag": "static/Botswana.png"},
    {"name": "Brazil", "flag": "static/Brazil.png"},
    {"name": "Brunei", "flag": "static/Brunei.png"},
    {"name": "Bulgaria", "flag": "static/Bulgaria.png"},
    {"name": "Burkina Faso", "flag": "static/Burkina Faso.png"},
    {"name": "Burundi", "flag": "static/Burnundi.png"},
    {"name": "Cabo Verde (Cape Verde)", "flag": "static/Cabo Verde.png"},
    {"name": "Cambodia", "flag": "static/Cambodia.png"},
    {"name": "Cameroon", "flag": "static/Cameroon.png"},
    {"name": "Canada", "flag": "static/Canada.png"},
    {"name": "Central African Republic", "flag": "static/Central African Republic.png"},
    {"name": "Chad", "flag": "static/Chad.png"},
    {"name": "Chile", "flag": "static/Chile.png"},
    {"name": "China", "flag": "static/China.png"},
    {"name": "Colombia", "flag": "static/Colombia.png"},
    {"name": "Comoros", "flag": "static/Comoros.png"},
    {"name": "Democratic Republic of the Congo", "flag": "static/Democratic Republic of the Congo.png"},
    {"name": "Republic of the Congo", "flag": "static/Republic of the Congo.png"},
    {"name": "Costa Rica", "flag": "static/Costa Rica.png"},
    {"name": "Côte d'Ivoire", "flag": "static/Côte d'Ivoire.png"},
    {"name": "Croatia", "flag": "static/Croatia.png"},
    {"name": "Cuba", "flag": "static/Cuba.png"},
    {"name": "Curaçao", "flag": "static/Curaçao.png"},
    {"name": "Cyprus", "flag": "static/Cyprus.png"},
    {"name": "Czech Republic", "flag": "static/Czech Republic.png"},
    {"name": "Denmark", "flag": "static/Denmark.png"},
    {"name": "Djibouti", "flag": "static/Djibouti.png"},
    {"name": "Dominica", "flag": "static/Dominica.png"},
    {"name": "Dominican Republic", "flag": "static/Dominican Republic.png"},
    {"name": "East Timor", "flag": "static/East Timor.png"},
    {"name": "Ecuador", "flag": "static/Ecuador.png"},
    {"name": "Egypt", "flag": "static/Egypt.png"},
    {"name": "El Salvador", "flag": "static/El Salvador.png"},
    {"name": "Equatorial Guinea", "flag": "static/Equatorial Guinea.png"},
    {"name": "Eritrea", "flag": "static/Eritrea.png"},
    {"name": "Estonia", "flag": "static/Estonia.png"},
    {"name": "Eswatini (SwazilandEsw)", "flag": "static/Eswatini.png"},
    {"name": "Ethiopia", "flag": "static/Ethiopia.png"},
    {"name": "Faroe Islands", "flag": "static/Faroe Islands.png"},
    {"name": "Fiji", "flag": "static/Fiji.png"},
    {"name": "Finland", "flag": "static/Finland.png"},
    {"name": "France", "flag": "static/France.png"},
    {"name": "Gabon", "flag": "static/Gabon.png"},
    {"name": "The Gambia", "flag": "static/The Gambia.png"},
    {"name": "Georgia", "flag": "static/Georgia.png"},
    {"name": "Germany", "flag": "static/Germany.png"},
    {"name": "Ghana", "flag": "static/Ghana.png"},
    {"name": "Greece", "flag": "static/Greece.png"},
    {"name": "Grenada", "flag": "static/Grenada.png"},
    {"name": "Greenland", "flag": "static/Greenland.png"},
    {"name": "Guadeloupe", "flag": "static/Guadeloupe.png"},
    {"name": "Guam", "flag": "static/Guam.png"},
    {"name": "Guatemala", "flag": "static/Guatemala.png"},
    {"name": "Guinea", "flag": "static/Guinea.png"},
    {"name": "Guinea-Bissau", "flag": "static/Guinea-Bissau.png"},
    {"name": "Guyana", "flag": "static/Guyana.png"},
    {"name": "Haiti", "flag": "static/Haiti.png"},
    {"name": "Honduras", "flag": "static/Honduras.png"},
    {"name": "Hungary", "flag": "static/Hungary.png"},
    {"name": "Iceland", "flag": "static/Iceland.png"},
    {"name": "India", "flag": "static/India.png"},
    {"name": "Indonesia", "flag": "static/Indonesia.png"},
    {"name": "Iran", "flag": "static/Iran.png"},
    {"name": "Iraq", "flag": "static/Iraq.png"},
    {"name": "Ireland", "flag": "static/Ireland.png"},
    {"name": "Israel", "flag": "static/Israel.png"},
    {"name": "Italy", "flag": "static/Italy.png"},
    {"name": "Jamaica", "flag": "static/Jamaica.png"},
    {"name": "Japan", "flag": "static/Japan.png"},
    {"name": "Jordan", "flag": "static/Jordan.png"},
    {"name": "Kazakhstan", "flag": "static/Kazakhstan.png"},
    {"name": "Kenya", "flag": "static/Kenya.png"},
    {"name": "Kiribati", "flag": "static/Kiribati.png"},
    {"name": "North Korea", "flag": "static/North Korea.png"},
    {"name": "South Korea", "flag": "static/South Korea.png"},
    {"name": "Kosovo", "flag": "static/Kosovo.png"},
    {"name": "Kuwait", "flag": "static/Kuwait.png"},
    {"name": "Kyrgyzstan", "flag": "static/Kyrgyzstan.png"},
    {"name": "Laos", "flag": "static/Laos.png"},
    {"name": "Latvia", "flag": "static/Latvia.png"},
    {"name": "Lebanon", "flag": "static/Lebanon.png"},
    {"name": "Lesotho", "flag": "static/Lesotho.png"},
    {"name": "Liberia", "flag": "static/Liberia.png"},
    {"name": "Libya", "flag": "static/Libya.png"},
    {"name": "Liechtenstein", "flag": "static/Liechtenstein.png"},
    {"name": "Lithuania", "flag": "static/Lithuania.png"},
    {"name": "Luxembourg", "flag": "static/Luxembourg.png"},
    {"name": "Macao", "flag": "static/Macao.png"},
    {"name": "Madagascar", "flag": "static/Madagascar.png"},
    {"name": "Malawi", "flag": "static/Malawi.png"},
    {"name": "Malaysia", "flag": "static/Malaysia.png"},
    {"name": "Maldives", "flag": "static/Maldives.png"},
    {"name": "Mali", "flag": "static/Mali.png"},
    {"name": "Malta", "flag": "static/Malta.png"},
    {"name": "Marshall Islands", "flag": "static/Marshall Islands.png"},
    {"name": "Mauritania", "flag": "static/Mauritania.png"},
    {"name": "Mauritius", "flag": "static/Mauritius.png"},
    {"name": "Mexico", "flag": "static/Mexico.png"},
    {"name": "Federated States of Micronesia", "flag": "static/Federated State of Micronesia.png"},
    {"name": "Moldova", "flag": "static/Moldova.png"},
    {"name": "Monaco", "flag": "static/Monaco.png"},
    {"name": "Mongolia", "flag": "static/Mongolia.png"},
    {"name": "Montenegro", "flag": "static/Montenegro.png"},
    {"name": "Morocco", "flag": "static/Morocco.png"},
    {"name": "Mozambique", "flag": "static/Mozambique.png"},
    {"name": "Myanmar (Burma)", "flag": "static/Myanmar.png"},
    {"name": "Namibia", "flag": "static/Namibia.png"},
    {"name": "Nauru", "flag": "static/Nauru.png"},
    {"name": "Nepal", "flag": "static/Nepal.png"},
    {"name": "Netherlands", "flag": "static/Netherlands.png"},
    {"name": "New Caledonia", "flag": "static/New Caledonia.png"},
    {"name": "New Zealand", "flag": "static/New Zealand.png"},
    {"name": "Nicaragua", "flag": "static/Nicaragua.png"},
    {"name": "Niger", "flag": "static/Niger.png"},
    {"name": "Nigeria", "flag": "static/Nigeria.png"},
    {"name": "Niue", "flag": "static/Niue.png"},
    {"name": "Northern Ireland", "flag": "static/Northern Ireland.png"},
    {"name": "Northern Mariana", "flag": "static/Northern Mariana.png"},
    {"name": "North Macedonia", "flag": "static/North Macedonia.png"},
    {"name": "Norway", "flag": "static/Norway.png"},
    {"name": "Oman", "flag": "static/Oman.png"},
    {"name": "Pakistan", "flag": "static/Pakistan.png"},
    {"name": "Palau", "flag": "static/Palau.png"},
    {"name": "Palestine", "flag": "static/Palestine.png"},
    {"name": "Panama", "flag": "static/Panama.png"},
    {"name": "Papua New Guinea", "flag": "static/Papua New Guinea.png"},
    {"name": "Paraguay", "flag": "static/Paraguay.png"},
    {"name": "Peru", "flag": "static/Peru.png"},
    {"name": "Philippines", "flag": "static/Philippines.png"},
    {"name": "Poland", "flag": "static/Poland.png"},
    {"name": "Portugal", "flag": "static/Portugal.png"},
    {"name": "Qatar", "flag": "static/Qatar.png"},
    {"name": "Romania", "flag": "static/Romania.png"},
    {"name": "Russia", "flag": "static/Russia.png"},
    {"name": "Rwanda", "flag": "static/Rwanda.png"},
    {"name": "Saba", "flag": "static/Saba.png"},
    {"name": "Saint Kitts and Nevis", "flag": "static/Sait Kitts and Nevis.png"},
    {"name": "Saint Lucia", "flag": "static/Saint Lucia.png"},
    {"name": "Saint Vincent and the Grenadines", "flag": "static/Saint Vincent and the Grenadines.png"},
    {"name": "Samoa", "flag": "static/Samoa.png"},
    {"name": "San Marino", "flag": "static/San Marino.png"},
    {"name": "São Tomé and Príncipe", "flag": "static/São Tomé and Príncipe.png"},
    {"name": "Saudi Arabia", "flag": "static/Saudi Arabia.png"},
    {"name": "Scotland", "flag": "static/Scotland.png"},
    {"name": "Senegal", "flag": "static/Senegal.png"},
    {"name": "Serbia", "flag": "static/Serbia.png"},
    {"name": "Seychelles", "flag": "static/Seychelles.png"},
    {"name": "Sierra Leone", "flag": "static/Sierra Leone.png"},
    {"name": "Singapore", "flag": "static/Singapore.png"},
    {"name": "Slovakia", "flag": "static/Slovakia.png"},
    {"name": "Slovenia", "flag": "static/Slovenia.png"},
    {"name": "Solomon Islands", "flag": "static/Solomon Islands.png"},
    {"name": "Somalia", "flag": "static/Somalia.png"},
    {"name": "South Africa", "flag": "static/South Africa.png"},
    {"name": "Spain", "flag": "static/Spain.png"},
    {"name": "Sri Lanka", "flag": "static/Sri Lanka.png"},
    {"name": "Sudan", "flag": "static/Sudan.png"},
    {"name": "South Sudan", "flag": "static/South Sudan.png"},
    {"name": "St. Eustatius", "flag": "static/St. Eustatius.png"},
    {"name": "St. Martin", "flag": "static/St. Martin.png"},
    {"name": "Suriname", "flag": "static/Suriname.png"},
    {"name": "Sweden", "flag": "static/Sweden.png"},
    {"name": "Switzerland", "flag": "static/Switzerland.png"},
    {"name": "Syria", "flag": "static/Syria.png"},
    {"name": "Taiwan", "flag": "static/Taiwan.png"},
    {"name": "Tajikistan", "flag": "static/Tajikistan.png"},
    {"name": "Tanzania", "flag": "static/Tanzania.png"},
    {"name": "Thailand", "flag": "static/Thailand.png"},
    {"name": "Togo", "flag": "static/Togo.png"},
    {"name": "Tonga", "flag": "static/Tonga.png"},
    {"name": "Trinidad and Tobago", "flag": "static/Trinidad and Tobago.png"},
    {"name": "Tunisia", "flag": "static/Tunisia.png"},
    {"name": "Turkey", "flag": "static/Turkey.png"},
    {"name": "Turkmenistan", "flag": "static/Turkmenistan.png"},
    {"name": "Tuvalu", "flag": "static/Tuvalu.png"},
    {"name": "Uganda", "flag": "static/Uganda.png"},
    {"name": "Ukraine", "flag": "static/Ukraine.png"},
    {"name": "United Arab Emirates", "flag": "static/United Arab Emirates.png"},
    {"name": "United Kingdom", "flag": "static/United Kingdom.png"},
    {"name": "United States of America", "flag": "static/United States of America.png"},
    {"name": "Uruguay", "flag": "static/Uruguay.png"},
    {"name": "Uzbekistan", "flag": "static/Uzbekistan.png"},
    {"name": "Vanuatu", "flag": "static/Vanuatu.png"},
    {"name": "Vatican City", "flag": "static/Vatican City.png"},
    {"name": "Venezuela", "flag": "static/Venezuela.png"},
    {"name": "Vietnam", "flag": "static/Vietnam.png"},
    {"name": "Wales", "flag": "static/Wales.png"},
    {"name": "Yemen", "flag": "static/Yemen.png"},
    {"name": "Zambia", "flag": "static/Zambia.png"},
    {"name": "Zimbabwe", "flag": "static/Zimbabwe.png"}
]

# Function to generate options randomly with the correct option included
def generate_options(correct_option):
    options = [correct_option]

    while len(options) < 3:
        new_option = f"Option{random.randint(1, 214)}"
        if new_option not in options:
            options.append(new_option)

    # Shuffle the options so that correct option in at a random postion
    random.shuffle(options)
    return [country['name'] for country in options] # Return only the names

# Function to get the correct option based on the country name
def get_correct_option(country_name):
    # Take the first letter of the country name as the correct answer
    return "Option" + country_name[0].upper()

# Function to start a new game session
def start_new_game():
    selected_country = random.choice(countries)
    correct_option = get_correct_option(selected_country['name'])
    selected_country['options'] = generate_options(correct_option)

    return selected_country

# Initial game setup
current_country = start_new_game()
game_active = False
correct_guesses = 0
incorrect_guesses = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    global game_active
    if not game_active:
        return redirect(url_for('index'))
    
    return render_template('game.html', country=current_country)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    global game_active, current_country, correct_guesses, incorrect_guesses

    data = request.get_json()
    selected_option = data.get('selectedOption')
    correct_option = data.get('correctOption')

    if selected_option == correct_option:
        response = {"message": "Correct! You guessed the flag correctly."}
        correct_guesses += 1
    else:
        response = {"message": "Incorrect. Try again!"}
        incorrect_guesses += 1

    current_country = start_new_game()
    game_active = True

    return jsonify(response)

@app.route('/start_game', methods=['POST'])
def start_game():
    global game_active, current_country, correct_guesses, incorrect_guesses

    game_active = True
    correct_guesses = 0
    incorrect_guesses = 0
    current_country = start_new_game()
    return jsonify({"flagUrl": current_country['flag'], "options": current_country['options']})



if __name__ == '__main__':
    app.run(debug=True)

