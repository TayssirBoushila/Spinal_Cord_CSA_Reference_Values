# Normalized CSA Reference Values - Method Comparison

## Overview
This project provides a web-based interface for comparing spinal cord cross-sectional area (CSA) reference values using two different methods: the consecutive nerve-based method and the vertebral-based method. The application is built using Streamlit and allows users to select specific parameters (level, sex, manufacturer, and height range) to retrieve and compare CSA reference values.

## Features
- **Parameter Selection**: Users can select the spinal level, sex, manufacturer, and height range.
- **Method Comparison**: Displays reference values for both the consecutive nerve-based and vertebral-based methods.
- **Confidence Intervals**: Provides confidence intervals for the mean CSA values for each method.

  
## How to Run the Application

To access the application, use the following URL:

[Spinal Cord CSA Reference Values](https://spinal-cord-csa-reference-values.streamlit.app/)

This URL provides access to the deployed Streamlit application where you can interact with the tool and view the normalized cervical spinal cord CSA reference values.

## Local Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/TayssirBoushila/Spinal_Cord_CSA_Reference_Values.git
    cd Spinal_Cord_CSA_Reference_Values
    ```

2. **Install the Required Packages**:
    Make sure you have Python installed. You can install the required dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    ```bash
    streamlit run site.py
    ```

4. **Access the Application**:
    Open your web browser and go to the URL provided by Streamlit, typically `http://localhost:8501`.

## Usage

Once the application is running, use the interface to:
- Select a spinal level, sex, manufacturer, and height range.
- View the reference CSA values for both methods.
- Compare the mean CSA and confidence intervals.

## Dataset
The dataset used in this project originates from the Spine Generic Database. This database provides MR images of the spinal cord, which have been used to derive the normalized cervical spinal cord CSA reference values included in this tool. The data has been processed and organized to allow for the comparison of different CSA measurement methods, facilitating research and clinical assessments.
The reference values are stored in the `merged_reference_values_csa.xlsx` file, which contains the following columns:
- `Level`: The spinal level.
- `Sex`: The sex of the subjects (Female/Male).
- `Manufacturer`: The MRI manufacturer (Siemens, GE, Philips).
- `Height_Range`: The height range in centimeters.
- `Mean_CSA_nerves`: The mean CSA value for the consecutive nerve-based method.
- `CI_Lower_nerves`: The lower bound of the confidence interval for the nerve-based method.
- `CI_Upper_nerves`: The upper bound of the confidence interval for the nerve-based method.
- `Mean_CSA_vertebral`: The mean CSA value for the vertebral-based method.
- `CI_Lower_vertebral`: The lower bound of the confidence interval for the vertebral-based method.
- `CI_Upper_vertebral`: The upper bound of the confidence interval for the vertebral-based method.

## Authors

  - **Tayssir Boushila** - *Lead Developer and Researcher*  
  Advanced Technologies for Medicine and Signals Lab, National Engineering School of Sfax, University of Sfax
  Sfax, Tunisia
  tayssirboushila3@gmail.com 
  GitHub: [TayssirBoushila](https://github.com/TayssirBoushila)

 - **Mouna Sahnoun** - *Co-Supervisor*  
  Higher institute of applied sciences and technologies, University of Gafsa, Gafsa, Tunisia,
  Advanced Technologies for Medicine and Signals Lab, National Engineering School of Sfax, University of Sfax,
  Sfax, Tunisia

- **Fathi Kallel** - *Thesis Director*  
  National School of Electronics and Communications, University of Sfax,
  Sfax, Tunisia,
  Advanced Technologies for Medicine and Signals Lab, National Engineering School of Sfax, University of Sfax,
  Sfax, Tunisia


## License

This project is licensed under the Creative Commons Attribution 4.0 International License. You are free to use, share, and adapt the content as long as you provide proper attribution to the original authors.




