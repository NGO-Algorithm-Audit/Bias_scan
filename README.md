# Fairness through discussion: A deliberative way forward

☁️ Implemented as an AWS web application, available on: https://www.algorithmaudit.eu/bias_scan/. 

📄 Details on legal background, statistical methods and use cases: [bias scan tool report](https://github.com/NGO-Algorithm-Audit/AI_Audit_Challenge/blob/master/Bias_scan_tool_report.docx).

## Why this bias scan?

- No data needed on protected attributes of users (unsupervised bias detection); 
- Model-agnostic (binary AI classifiers); 
- Developed open-source and not-for-profit.

## Executive summary
Artificial intelligence (AI) is increasingly used to automate or support policy decisions that affects individuals. It is imperative that AI adheres to the legal and ethical requirements on such policy decisions. In particular, policy decisions should not be systematically discriminatory (direct or indirect) with respect to protected attributes such as gender, sex, or race.

To achieve this, we propose a scalable, model-agnostic, and open-source bias scan tool to identify potentially discriminated groups of similar users in AI systems. This bias scan tool does not require *a priori* information about existing disparities and sensitive attributes, and is therefore able to detect possible proxy discrimination, intersectional discrimination and other types of differentiation that evade non-discrimination law. The tool is implemented on the [website](https://www.algorithmaudit.eu/bias_scan/) of NGO Algorithm Audit, such that it can be used by a wide public.

As demonstrated on a BERT-based Twitter disinformation detection model, the bias scan tool identifies statistically significant disinformation classification bias against users with an unverified profile and an above average number of mentions and hashtags used in tweets. On the German Credit data set, statistically significant loan approval bias is observed on the basis of applicants’ job status, telephone registration and the amount of credit requested. 

These observations do not establish prohibited *prima facie* discrimination. Rather, the identified disparities serve as a starting point to assess potential discrimination according to the context-sensitive legal doctrine, i.e., assessment of the legitimacy of the aim pursued and whether the means of achieving that aim are appropriate and necessary. For this qualitative assessment, we propose an expert-oriented deliberative method. Which allows policy makers, journalist, data subjects and other stakeholders to publicly review identified quantitative disparities against the requirements of non-discrimination law and ethics. In our two-pronged quantitative-qualitative solution, scalable statistical methods work in tandem with the normative capabilities of human subject matter experts to define fair AI on a case-by-case basis. 

\* <sub>The implemented bias scan tool is based on the k-means Hierarchical Bias-Aware Clustering (HBAC) method as described in Misztal-Radecka, Indurkya, *Information Processing and Management*. Bias-Aware Hierarchical Clustering for detecting the discriminated groups of users in recommendation systems (2021).</sub>

## Solution
![image](./images/Quantitative_qualitatitive.png)

## Results
![image](./images/Bias_scan_BERT_disinfo_classifier.png)
![image](./images/Bias_scan_XGBoost_loan_approval_classifier.png)

### Structure of this repository
```
    .
    ├── bias_scan_tool              # Bias scan tool 
    ├── classification_models       # Classifiers
    ├── data                        # Twitter and credit data sets
    ├── images                      # Images
    ├── literature                  # Reference materials
    ├── .gitattributes              # To store large files
    ├── .gitignore                  # Files to be ignored in this repo
    ├── Bias_scan_tool_report.pdf   # Main deliverable
    ├── LICENSE                     # MIT license for sharing 
    └── README.md                   # Read me file 
    
```


## This submission is endorsed by
- Jurriaan Parie, Trustworthy AI data scientist at IBM
- Ariën Voogt, PhD-candidate in Philosophy at Protestant Theological University of Amsterdam
- dr. Vahid Niamadpour, PhD-candidate in Linguistics at Leiden University
- ...