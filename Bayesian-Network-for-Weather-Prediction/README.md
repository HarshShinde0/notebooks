# Bayesian Network for Weather Prediction

This project implements a **Bayesian Network model for weather prediction** using the [pgmpy](https://pgmpy.org/) library in Python. The Bayesian Network represents the relationship between weather outlook (such as sunny, overcast, or rainy) and the occurrence of rain. By defining **Conditional Probability Distributions (CPDs)** for these variables, the model can predict the likelihood of rain given a specific weather outlook.

## 📈 Description

- **Structure:**  
  The Bayesian Network consists of two variables:
  - `Outlook` (with states: sunny, overcast, rainy)
  - `Rain` (with states: yes, no)
  - The relationship is defined as: `Outlook → Rain`

- **CPDs:**  
  Conditional Probability Distributions are defined for both `Outlook` and `Rain`, describing the probability of each state and how likely rain is under each type of outlook.

- **Model Validation:**  
  The model is validated for consistency to ensure all probabilities are correctly defined and sum to 1.

- **Inference:**  
  Using `pgmpy`'s inference engine, the model predicts the probability of rain for each outlook scenario—demonstrating how **Bayesian reasoning** can be used for decision-making in weather forecasting.

- **Practical Application:**  
  This notebook showcases the practical application of Bayesian Networks in **probabilistic reasoning** and **decision-making**, providing a template for extending to more complex real-world weather or risk prediction problems.

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install pgmpy
```

### 2. Run the Example

The following code block shows how to define, validate, and use the Bayesian Network:

```python
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the Bayesian Network structure
model = BayesianModel([('Outlook', 'Rain')])

# Define CPDs
cpd_outlook = TabularCPD(
    variable='Outlook', variable_card=3, 
    values=[[0.4], [0.3], [0.3]],
    state_names={'Outlook': ['sunny', 'overcast', 'rainy']}
)
cpd_rain = TabularCPD(
    variable='Rain', variable_card=2, 
    values=[[0.8, 0.4, 0.2], [0.2, 0.6, 0.8]],
    evidence=['Outlook'], evidence_card=[3],
    state_names={'Rain': ['yes', 'no'], 'Outlook': ['sunny', 'overcast', 'rainy']}
)

# Add CPDs to the model
model.add_cpds(cpd_outlook, cpd_rain)

# Check model for consistency
print("Model is consistent:", model.check_model())

# Perform inference
inference = VariableElimination(model)
for outlook in ['sunny', 'overcast', 'rainy']:
    query = inference.query(variables=['Rain'], evidence={'Outlook': outlook})
    print(f"Predicted probability of rain given {outlook} outlook:", query.values[0])
```

#### **Expected Output**
```
Model is consistent: True
Predicted probability of rain given sunny outlook: 0.8
Predicted probability of rain given overcast outlook: 0.4
Predicted probability of rain given rainy outlook: 0.2
```

---

## 📚 References

- [pgmpy Documentation](https://pgmpy.org/)
- [Bayesian Networks (Wikipedia)](https://en.wikipedia.org/wiki/Bayesian_network)

---

## 🙋‍♂️ Author

- **Harsh Shinde**  
  [GitHub Profile](https://github.com/HarshShinde0)

---

*If you found this project helpful, please ⭐ star the repository!*


