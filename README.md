# Fairness through discussion: A deliberative way forward

The main deliverable of this submission: [NGO Algorithm Audit – Bias scan tool report](https://github.com/NGO-Algorithm-Audit/AI_Audit_Challenge/blob/master/report/Report_AI_Audit_Challenge.docx)

Structure of this repository.

```
    .
    ├── bias_scan_tool          # Bias scan code 
    ├── data                    # Data sets
    ├── literature              # Reference materials
    ├── report                  # Main document
    ├── .gitattributes          # To store large files
    ├── .gitignore              # Files to be ignored in this repo
    ├── LICENSE                 # MIT license for sharing 
    └── README.md               # Read me file
```
## Summary
Fairness cannot be automated. As AI is omnipresent in digital society, there is an urgent need to review AI systems with respect to the qualitative requirements of law and ethics. To facilitate this endeavour, we propose a scalable, easy to use, and open-source bias scan tool. This bias scan tool identifies potentially discriminated groups of similar users in AI systems (including proxy and intersectional discrimination) and requires no a priori information about existing disparities and sensitive attributes. As demonstrated on a BERT-based Twitter disinformation detection model, the bias scan tool identifies statistically significant disinformation classification bias on the basis of verified user profiles, the number of mentions and hashtags used in tweets. On a widely cited credit data set, statistically significant loan approval bias is observed on the basis of applicants’ job status, telephone registration and the amount of credit requested. These observations do not establish prima facie algorithmic discrimination. Rather, the identified disparities serve as a starting point to assess potential discrimination according to the context-sensitive legal doctrine, i.e., assessment of the legitimacy, proportionality, and indispensability of the observed disparities. For this qualitative assessment, we propose an expert-led deliberative method to review identified quantitative disparities. In this manner, scalable statistical methods work in tandem with the normative capabilities of the legal paradigm to define fair AI on a case-by-case basis.

## Contributors
- Jurriaan Parie, Trustworthy AI data scientist at IBM
- Ariën Voogt, PhD-candidate in Philosophy at Protestant Theological University of Amsterdam
- dr. Vahid Niamadpour, PhD-candidate in Linguistics at Leiden University