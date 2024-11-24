import os
import requests
import datetime
import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
from dash import *
import dash_daq as daq
from flask import Flask, send_from_directory
from dotenv import load_dotenv
import datetime
import pytz


def configure():
    load_dotenv()

# Initialize Dash app with Font Awesome for icons
app = dash.Dash(__name__, 
                # prevent_initial_callbacks=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP, "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"])
app.title = "About Kevin Baliat"

server = app.server
# Color Theme
colors = {
    "primary": "#191970",  # Dark Blue
    "secondary": "#F08000",  # Green
    "background": "#ECF0F1",  # Light Gray
    "text": "#34495E",  # Darker Text
}

# OpenWeatherMap API setup
LAT = 34.0522  # Latitude for Los Angeles
LON = -118.2437  # Longitude for Los Angeles
# WEATHER_URL = f"http://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=imperial"

city = "Los Angeles"

configure()
WEATHER_URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=imperial'

# Function to fetch weather data
def fetch_weather():
    try:
        response = requests.get(WEATHER_URL)
        data = response.json()
        temperature = round(data["main"]["temp"])
        weather_desc = data["weather"][0]["description"].capitalize()
        icon = data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon}.png"
        return f"Weather in {city}: {temperature}°F, {weather_desc}", icon_url
    except Exception:
        print(f'[ERROR]\t ERROR GETTING WEATHER: {Exception}')
        return "Unavailable", ""

# Header with time and weather
header = dbc.Row(
    [
        dbc.Col(
            html.Div(
                [
                    html.H1("Kevin Baliat", className="text-white mb-0"),
                    html.H4("Data Scientist | Life Sciences & Manufacturing", className="text-white"),
                ],
                className="p-4",
            ),
            width=9,
        ),
        dbc.Col(
            html.Div(
                id="time-weather-container",
                className="d-flex flex-column align-items-end justify-content-center p-4",
            ),
            width=3,
        ),
        dbc.Col(# Dark Mode Toggle Switch
        html.Div(
            [
                html.Label("Dark Mode", style={"color": "#fff"}),
                daq.BooleanSwitch(  # DAQ BooleanSwitch component for dark mode
                    id="dark-mode-toggle",
                    on=False,  # Default to light mode
                    style={"marginTop": "10px"},
                    color="rgb(50, 205, 50)",  # Green color for the switch
                ),
            ],
            style={"position": "fixed", "bottom": "20px", "right": "20px"},
        ),)
    ],
    className="align-items-center",
    style={"backgroundColor": colors["primary"], "borderRadius": "10px"},
)

# Skills Section without Icons
skills_content = html.Div(
    [
        html.H4(
            "Skills",
            style={"color": colors["secondary"], "marginBottom": "20px"},
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Ul(
                        [
                            html.Li("Machine Learning"),
                            html.Li("Statistical Modeling"),
                            html.Li("Visualization in R"),
                        ],
                        style={"listStyleType": "none", "padding": 0, "margin": 0},
                    ),
                    width=4,
                ),
                dbc.Col(
                    html.Ul(
                        [
                            html.Li("Python"),
                            html.Li("SQL"),
                            html.Li("Tableau"),
                        ],
                        style={"listStyleType": "none", "padding": 0, "margin": 0},
                    ),
                    width=4,
                ),
                dbc.Col(
                    html.Ul(
                        [
                            html.Li("Databricks"),
                            html.Li("Plotly Dash"),
                            html.Li("UiPath"),
                        ],
                        style={"listStyleType": "none", "padding": 0, "margin": 0},
                    ),
                    width=4,
                ),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        "Languages: Swahili, English",
                        className="text-center",
                        style={"fontWeight": "bold", "marginTop": "10px"},
                    ),
                    width=12,
                ),
            ],
        ),
    ],
    className="p-4",
    style={"backgroundColor": "white", "borderRadius": "10px"},
)

# Now update the "Professional" tab to include the new skills container
professional_content = html.Div(
    [
        html.Br(),
        html.H4(
            [html.I(className="fas fa-briefcase me-2"), "Professional Experience"],
            style={"color": colors["secondary"]},
        ),
        html.Div(
            [
                html.H5("Data Scientist at Amgen, Thousand Oaks, CA (Sep 2022 – Present)", className="fw-bold"),
                html.Ul(
                    [
                        html.Li(
                            "Product owner for all Plotly Dash web applications within the Digital Manufacturing & Clinical Supply team."
                        ),
                        html.Li(
                            "Developed a validated application to support timely generation of reports related to raw materials and supplier information, improving efficiency by 90%."
                        ),
                        html.Li(
                            "Built a Contamination Control Tracker that streamlined and provided visibility into microbial contaminations."
                        ),
                        html.Li(
                            "Created an Inventory scan and compare tool that allowed warehouse users to track scanned inventory and compare counts with SAP inventory in real-time, improving productivity by ~70%."
                        ),
                        html.Li(
                            "Designed a Master Production Schedule (MPS) tool to enhance planning, including scenario analysis, easy updates to master data, and identification of scheduling conflicts by highlighting equipment overlaps."
                        ),
                        html.Li(
                            "Developed a GenAI chatbot using Llama Index and OpenAI for the Contamination Control Tracker, addressing user inquiries about contaminations and CAPAs."
                        ),
                        html.Li(
                            "Implemented Robotic Process Automation (RPA) solutions with UiPath to automate business processes, driving notable productivity improvements."
                        ),
                    ]
                ),
                html.H5("Associate, Career Discovery Rotational Program (CDP) at Amgen (July 2020 – Sep 2022)", className="fw-bold"),
                html.Ul(
                    [
                        html.Li("Rotation #3: Operations Advance Analytics (OAA) – Operations (January 2022 – September 2022)"),
                        html.Ul(
                            [
                                html.Li(
                                    "Developed a Workforce Planning POC to automate and optimize labor allocation for manufacturing operations."
                                ),
                                html.Li(
                                    "Built dynamic prototypes connected to backend source systems for two Ireland manufacturing teams, enabling strategic planners to track workloads and forecast headcount requirements."
                                ),
                                html.Li(
                                    "Designed Tableau and interactive Plotly Dash dashboards to help managers identify capacity pinch-points and allocate resources accordingly."
                                ),
                            ]
                        ),
                        html.Li("Rotation #2: Commercial Data & Analytics - Oncology Forecasting (April 2021 – January 2022)"),
                        html.Ul(
                            [
                                html.Li(
                                    "Developed a peak revenue estimation tool for early-stage oncology assets using exponential regression, machine learning, and epidemiology-based models."
                                ),
                                html.Li(
                                    "Conducted exploratory analysis of oncology brand revenues in China, deriving revenue multipliers and analyzing trends around Loss of Exclusivity (LOE) and generic drug performance."
                                ),
                                html.Li(
                                    "Compared Amgen’s market outlook with external analyst views to improve forecasting accuracy with enriched insights."
                                ),
                            ]
                        ),
                        html.Li("Rotation #1: Anti-Bribery/Anti-Corruption (ABAC) & Risk Assessments (July 2020 – April 2021)"),
                        html.Ul(
                            [
                                html.Li(
                                    "Analyzed ABAC training data to assess effectiveness, providing actionable insights for program improvements."
                                ),
                                html.Li(
                                    "Consolidated in-house risk assessments with the Global Risk Assessment team, enabling data-driven resource allocation."
                                ),
                                html.Li(
                                    "Developed and deployed surveys in PEGA Platform, tracking progress and submissions."
                                ),
                            ]
                        ),
                    ]
                ),
                html.H5("Global Trade Compliance (GTC) Intern at Amgen, Thousand Oaks, CA (June 2019 – Aug 2019)", className="fw-bold"),
                html.Ul(
                    [
                        html.Li(
                            "Created a visual tool to rank global manufacturing and affiliate sites by trade data privacy risk."
                        ),
                        html.Li(
                            "Implemented a quarterly monitoring program to gather trade metadata and report findings to stakeholders."
                        ),
                        html.Li(
                            "Designed a centralized Global Trade Compliance data intelligence survey for annual monitoring."
                        ),
                        html.Li(
                            "Collaborated with Compliance Analytics and Risk teams to adopt risk assessment tools for Key Risk Indicators (KRIs)."
                        ),
                    ]
                ),
                html.H5("Research Assistant, Royal Holloway Economics Department, Egham, UK (Feb 2019 – May 2019)", className="fw-bold"),
                html.Ul(
                    [
                        html.Li(
                            "Digitized agricultural data (1935–1955) from the National Archives for analysis in Stata."
                        ),
                        html.Li(
                            "Defined key variables and examined regional food supply variations for research presentation."
                        ),
                        html.Li(
                            "Supported a presentation at the Scottish Economics Society Conference."
                        ),
                    ]
                ),
                html.H5("Accounts Payable Intern, Vassar College (Aug 2018 – Dec 2018)", className="fw-bold"),
                html.Ul(
                    [
                        html.Li(
                            "Assisted accounting operations with Workday transactions, bank reconciliation, and check voiding/reissuing."
                        ),
                        html.Li(
                            "Updated investment market value balance sheets using current data."
                        ),
                        html.Li(
                            "Managed outstanding checks for students and faculty through reminders and follow-ups."
                        ),
                    ]
                ),
            ],
            className="p-4",
            style={"backgroundColor": "white", "borderRadius": "10px"},
        ),

        html.Div(
            skills_content,  # Skills container 
            style={'margin':'10px'}
        )
        
    ]
)

# About Me tab content

# Serving static files (images)
gallery_path = "data/gallery_images"

## Add a Flask route to serve images
@app.server.route("/data/gallery_images/<path:filename>")
def serve_gallery_images(filename):
    return send_from_directory(gallery_path, filename)

# Function to load gallery images dynamically
def load_gallery_images():
    images = []
    if os.path.exists(gallery_path):
        for idx, file in enumerate(sorted(os.listdir(gallery_path))):
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                label = f"{file.split('.')[0].replace('_', ' ').capitalize()}" #mage {idx + 1}: 
                images.append(
                    dbc.Card(
                        [
                            dbc.CardImg(
                                src=f"/data/gallery_images/{file}",
                                top=True,
                                style={"height": "200px", "objectFit": "cover"},
                            ),
                            dbc.CardBody(
                                html.P(label, className="text-center"),
                                className="p-2",
                            ),
                        ],
                        className="m-2 shadow-sm",
                        style={"width": "18rem"},
                    )
                )
    return images

# About Me content
about_me_content = html.Div(
    [
        html.H4(
            [html.I(className="fas fa-user me-2"), "About Me"],
            style={"color": colors["secondary"]},
        ),
        html.P(
            """
            I’m a data scientist with a passion for turning data into actionable insights that drive meaningful results. My 
            expertise lies in machine learning, statistical modeling, and visual analytics, with a focus on operational efficiency 
            and strategic forecasting. I’ve honed these skills in life sciences and manufacturing, delivering impactful solutions 
            like workforce planning tools, oncology revenue forecasts, and compliance risk assessments. 

            As a product owner, I’ve successfully led the development of web applications using Plotly Dash and Posit Connect, 
            as well as RPA solutions with UiPath that streamline workflows and enhance productivity. I take pride in bridging the 
            gap between complex data and practical solutions that make a real difference.

            Outside of work, I enjoy playing soccer, exploring scenic hiking trails, and traveling to experience new cultures and cuisines.
            """,
            style={"textAlign": "justify", "lineHeight": "1.6"},
        ),
        html.H4(
            [html.I(className="fas fa-graduation-cap me-2"), "Education"],
            style={"color": colors["secondary"]},
        ),
        html.Ul(
            [
                html.Li("Bachelor of Arts in Mathematics and Statistics, Vassar College"),
                html.Li("President of the African Students Union at Vassar College"),
                html.Li("Recipient of The Shirley Oakes Butler Fund."),
            ]
        ),
        html.H4(
            [html.I(className="fas fa-futbol me-2"), "Interests"],
            style={"color": colors["secondary"]},
        ),
        html.Ul(
            [
                html.Li("Soccer (All-Liberty League Second Team Honor)"),
                html.Li("Travel"),
                html.Li("Scenic hikes"),
                html.Li("Data-driven storytelling for impactful insights"),
            ]
        ),
        html.H4(
            [html.I(className="fas fa-address-book me-2"), "Contacts"],
            style={"color": colors["secondary"]},
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.I(className="fas fa-envelope me-2", style={"color": colors["secondary"]}),
                            html.Span("Email: "),
                            html.A("kevinbaliat@gmail.com", href="mailto:kevinbaliat@gmail.com", className="text-primary"),
                        ],
                        className="mb-2",
                        style={'margin-left':'10px'}
                    ),
                    width=12,
                ),
                dbc.Col(
                    html.Div(
                        [
                            html.I(className="fab fa-linkedin me-2", style={"color": colors["secondary"]}),
                            html.Span("LinkedIn: "),
                            html.A("linkedin.com/in/kevin-baliat", href="www.linkedin.com/in/kevin-baliat", target="_blank", className="text-primary"),
                        ],
                        className="mb-2",
                        style={'margin-left':'10px'}

                    ),
                    width=12,
                ),
            ],
        ),
        html.H4(
            [html.I(className="fas fa-images me-2"), "Gallery"],
            style={"color": colors["secondary"], 'margin-bottom':'30px', 'margin-top':'20px'},
        ),
        dbc.Row(
            load_gallery_images(),
            className="g-3",
            style={"display": "flex", "justifyContent": "center"},
        ),
    ],
    className="p-4",
    style={"backgroundColor": "white", "borderRadius": "10px"},
)

# Main app layout

# Add an interval component to trigger updates
interval_component = dcc.Interval(
    id="interval-component",
    interval=60000,  # Update every minute
    n_intervals=0,
)

# Add Footer to the app layout
footer = html.Div(
    [
        html.P(
            "Curated by Kevin Baliat using Plotly Dash",
            className="text-center text-white p-3",
            style={
                "backgroundColor": colors["primary"],
                "position": "fixed",
                "bottom": "0",
                "width": "100%",
                "margin": "0",
                "fontSize": "14px",
            },
        )
    ]
)

# Add footer to the main layout
app.layout = dbc.Container(
    [
        header,
        interval_component,
        dbc.Tabs(
            [
                dbc.Tab(about_me_content, label="About Me", tab_id="tab-about-me", activeTabClassName="fw-bold text-primary"),
                dbc.Tab(professional_content, label="Professional", tab_id="tab-professional", activeTabClassName="fw-bold text-primary"),

            ],
            id="tabs",
            active_tab="tab-about-me",
            className="mt-4",
        ),
        footer,  # Footer added here
    ],
    fluid=True,
    id="app-container",  # ID to target for background color
    style={"backgroundColor": "#f4f4f9", "padding": "20px"},  # Light mode default background
)
#------------------------------------------------------

# Callback for updating time and weather
@app.callback(
    Output("time-weather-container", "children"),
    Input("interval-component", "n_intervals"),
)
def update_time_and_weather(_):
    # Get live time
    # Los Angeles Timezone (PST or PDT depending on daylight saving)
    la_timezone = pytz.timezone("America/Los_Angeles")
    
    # Get the current time in UTC, then convert to Los Angeles time
    now_utc = datetime.datetime.now(pytz.utc)
    now_la = now_utc.astimezone(la_timezone)
    
    # Format the time as required
    formatted_time = now_la.strftime("%A, %B %d, %I:%M %p %Z")

    # Get weather details
    weather, icon_url = fetch_weather()

    # Apply CSS filter to make the icon white
    icon_style = {
        "height": "40px",
        "marginRight": "5px",
        "filter": "invert(100%)",  # Apply invert filter to turn icon white
    }

    return [
        html.Div(formatted_time, className="text-white text-end fw-bold mb-2"),
        html.Div(
            [
                html.Img(src=icon_url, style=icon_style) if icon_url else None,
                html.Span(weather, className="text-white"),
            ],
            className="d-flex align-items-center",
        ),
    ]

#------------------------------------------------------

# Callback to toggle dark mode

# Run app
if __name__ == "__main__":
    app.run_server(debug=True)
