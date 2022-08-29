# Fair AI through discussion: A deliberative way forward

The main deliverable of this submission is: [bias scan tool report](https://github.com/NGO-Algorithm-Audit/AI_Audit_Challenge/blob/master/report/Report_AI_Audit_Challenge.docx).

## Summary
Fairness cannot be automated. As AI is omnipresent in digital society, there is an urgent need to review AI systems with respect to the qualitative requirements of law and ethics. To facilitate this time-consuming endeavour, we propose a scalable, easy to use, and open-source bias scan tool to identify potentially discriminated groups of similar users in AI systems. This bias scan tool does not require a priori information about existing disparities and sensitive attributes, and is therefore able to detect potential proxy discrimination, intersectional discrimination and new types of differentiation that evade non-discrimination law. 

- As demonstrated on a BERT-based Twitter disinformation detection model, the bias scan tool identifies statistically significant disinformation classification bias on the basis of verified user profiles, the number of mentions and hashtags used in tweets. 
- On the widely cited German Credit data set, statistically significant loan approval bias is observed on the basis of applicants’ job status, telephone registration and the amount of credit requested. 

These observations do not establish prima facie algorithmic discrimination. Rather, the identified disparities serve as a starting point to assess potential discrimination according to the context-sensitive legal doctrine, i.e., assessment of the legitimacy of the aim pursued and whether the means of achieving that aim are appropriate and necessary. For this qualitative assessment, we propose an expert-led deliberative method to review identified quantitative disparities against the requirements of non-discrimination law and ethics. In this manner, scalable statistical methods work in tandem with the normative capabilities of human subject matter experts to define fair AI on a case-by-case basis.


![image](./images/HBAC_disinformation.png)
![image](./images/HBAC_loan_approval.png)

### Structure of this repository
```
    .
    ├── bias_scan_tool          # Bias scan tool 
    ├── classification_models   # Classifiers
    ├── data                    # Twitter and credit data sets
    ├── images                  # Images
    ├── literature              # Reference materials
    ├── LICENSE                 # MIT license for sharing 
    ├── report                  # Main deliverable
    ├── README.md               # Read me file 
    ├── .gitattributes          # To store large files
    └── .gitignore              # Files to be ignored in this repo
```


## Contributors
- Jurriaan Parie, Trustworthy AI data scientist at IBM
- Ariën Voogt, PhD-candidate in Philosophy at Protestant Theological University of Amsterdam
- dr. Vahid Niamadpour, PhD-candidate in Linguistics at Leiden University