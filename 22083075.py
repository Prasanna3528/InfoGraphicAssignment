import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as patches
from matplotlib import rcParams

# Setting font to Times New Roman
rcParams['font.family'] = 'Times New Roman'

#Function to add borders around the plots
def addborder(ax, width=3, color='black'):
    """Add a border around the axes."""
    rect = patches.Rectangle(
        (0, 0), 1, 1, transform=ax.transAxes,
        linewidth=width, edgecolor=color, facecolor='none'
    )
    ax.add_patch(rect)


# Reading Data from CSV
enroll = pd.read_csv('Net Enroll.csv')
pt_ratio = pd.read_csv('P-T Ratio.csv')
gdp_exp = pd.read_csv('GDP Exp.csv')
literacy = pd.read_csv('LiteracyRate.csv')

# Defining Colors from the color pallette
colors = {
    'Primary': '#e17c05', 'Secondary': '#6a3d9a', 
    'Tertiary': '#b15928', 'Male': '#ff7f00', 
    'Female': '#cab2d6', 'GDP Exp': '#33a02c', 
    'Bar': '#a6cee3'
}

# Initialize Figure and Grid
fig = plt.figure(figsize=(20, 24), facecolor='#E6E6FA')
gs = gridspec.GridSpec(
    4, 3, height_ratios=[1.5, 1.5, 1.5, 2]
)

#Adding Main title to the Visualisation
plt.suptitle(
    "Evolution of Education: A 50-Year Statistical Review in the UK", 
    fontsize=40, fontweight='bold', y=0.96
)


def format_axes(ax, xlabel, ylabel, title):
    """
    Formats the axes of a matplotlib plot.

    Parameters:
    - ax (matplotlib.axes.Axes): The axes object to be formatted.
    - xlabel (str): The label for the x-axis.
    - ylabel (str): The label for the y-axis.
    - title (str): The title of the plot.

    Returns:
    None
    
    """
    ax.set_xlabel(xlabel, fontsize=20, fontweight='bold', labelpad=20)
    ax.set_ylabel(ylabel, fontsize=20, fontweight='bold', labelpad=20)
    ax.set_title(title, fontsize=25, fontweight='bold', pad=20)

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(18)
        label.set_fontweight('bold')

    legend = ax.legend(prop={'size': 18, 'weight': 'bold'})
    if legend:
        legend.get_title().set_fontsize('18')
        legend.get_title().set_fontweight('bold')



# Net Enrollment Rate Plot
graph1 = plt.subplot(gs[1, :1])
E_Year = enroll['Year']
graph1.plot(
    E_Year, enroll['Primary'], label='Primary', 
    color=colors['Primary'], linewidth=4
)
graph1.plot(
    E_Year, enroll['Secondary'], label='Secondary', 
    color=colors['Secondary'], linewidth=4
)
graph1.plot(
    E_Year, enroll['Tertiary'], label='Tertiary', 
    color=colors['Tertiary'], linewidth=4
)
graph1.set_xticks(E_Year)
graph1.set_xticklabels(E_Year, ha="center")
graph1.legend(prop={'size': 14, 'weight': 'bold'})
addborder(graph1)
format_axes(
    graph1, 'Year', 'Net Enrollment Rate (%)', 'Net Enrollment Rate'
)

# Pupil-Teacher Ratio Plot
graph0 = plt.subplot(gs[0, :])
ind = np.arange(len(pt_ratio))
width = 0.25
graph0.bar(
    ind - width, pt_ratio['Primary'], width, label='Primary', 
    color=colors['Primary']
)
graph0.bar(
    ind, pt_ratio['Secondary'], width, label='Secondary', 
    color=colors['Secondary']
)
graph0.bar(
    ind + width, pt_ratio['Tertiary'], width, label='Tertiary', 
    color=colors['Tertiary']
)
graph0.set_xticks(ind)
graph0.set_xticklabels(pt_ratio['Year'].astype(str))
graph0.legend()
addborder(graph0)
format_axes(
    graph0, 'Year', 'Pupil-Teacher Ratio', 
    'Pupil-Teacher Ratio by Education Level and Year'
)


# Government Expenditure Pie Charts
def create_pie_chart(ax, year, data):
    """
    Creates a pie chart to visualize government expenditure as a percentage of GDP for a given year.

    Parameters:
    - ax (matplotlib.axes.Axes): The axes object on which the pie chart will be plotted.
    - year (int): The specific year for which the government expenditure data is visualized.
    - data (pandas.DataFrame): The DataFrame containing government expenditure data.

    Returns:
    None

    """
    gdp = data[data['Year'] == year]['GDP Exp'].iloc[0]
    sizes = [gdp, 100 - gdp]
    labels = ['Education', 'Other']
    ax.pie(
        sizes, labels=labels, autopct='%1.1f%%', startangle=140, 
        textprops={'fontsize': 14, 'weight': 'bold'}
    )
    ax.axis('equal')
    ax.set_title(
        f'{year} Gov. Expenditure (% of GDP)', fontsize=20, 
        fontweight='bold', pad=20
    )



graphpie1 = plt.subplot(gs[1, 1])
graphpie2 = plt.subplot(gs[1, 2])
create_pie_chart(graphpie1, 1970, gdp_exp)
create_pie_chart(graphpie2, 2020, gdp_exp)
addborder(graphpie1)
addborder(graphpie2)

# Literacy Rate Plot
graph3 = plt.subplot(gs[2, :])
positions = np.arange(len(literacy)) * 0.15
graph3.bar(
    positions, literacy['Male'], width=0.05, label='Male', 
    color=colors['Male']
)
graph3.bar(
    positions, literacy['Female'], width=0.05, bottom=literacy['Male'], 
    label='Female', color=colors['Female']
)
graph3.set_xticks(positions)
graph3.set_xticklabels(literacy['Year'].astype(str))
graph3.legend()
addborder(graph3)
format_axes(
    graph3, 'Year', 'Literacy Rate (%)', 'Literacy Rate by Gender'
)
plt.setp(
    graph3.get_xticklabels(), ha="center", rotation_mode="anchor"
)

# Adding Summary Text Subplot
grid4 = plt.subplot(gs[3, :])
grid4.axis('off')
grid_text = (
    "- Education expenditure as a percentage of GDP rose by 9.25% over "
    "50 years, paralleling notable improvements in literacy rates, with "
    "male literacy increasing by 20.88% and female literacy by 47.23%, "
    "highlighting strides in gender equality in education.\n\n"
    "- While primary school enrollment saw a slight decrease of 5.15%, "
    "secondary and tertiary enrollments surged by 54.67% and 364.46%, "
    "respectively, reflecting a significant shift towards higher education."
    "\n\n"
    "- The decrease in the pupil-teacher ratio by 24.86% in primary schools "
    "suggests improvements in educational quality, but the increase in "
    "ratios at secondary (33.07%) and tertiary (67.60%) levels points to "
    "ongoing challenges in teacher availability as education levels advance."
    "\n\n"
    "- Overall, these trends indicate a positive trajectory in educational "
    "engagement and access, especially in reducing gender disparities, but "
    "also emphasize the need for consistent investment in educational "
    "infrastructure and resources to sustain and enhance these outcomes."
)
grid4.text(
    0, 0.5, grid_text, ha='left', va='center', fontsize=25, 
    color='black', wrap=True
)

# adding Name and ID
plt.figtext(
    0.95, 0.02, "Name:Lakshmi Prasanna Mandava \n ID:22083075 ", ha="right", fontsize=20, color='black'
)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
