# AI Unlocked: Empowering Higher Ed through Research and Discovery  
## **Presenter Guide: Uploading Your Materials**  

Welcome to the **AI Unlocked Workshop Repository!** As a presenter, please follow these guidelines to upload your materials and make them accessible to participants.  

### **Recommended Folder Structure**  
We recommend organizing your session materials within your respective track folder:  
- **Beginner Track:** `track1-beginner/`
- **Intermediate to Advanced Track:** `track2-advanced/`

Each session can have its own subfolder with relevant materials. While presenters are free to organize their materials, we **recommend** the following structure for ease of navigation, it is **highly recommended** to include:  
- **Presentation slides** (`slides.pdf` or `.pptx`)  
- **Workshop notes or instructions** (`workshop-notes.md`)  
- **Code files** (`.py`, `.sh`, or other source files in a `code/` folder)  
- **Jupyter Notebooks** (`.ipynb` in a `notebooks/` folder)  
- **Setup instructions** (`setup-instructions.md`) for running materials on different resources (e.g., Delta, Expanse)  

You are free to structure your session materials in a way that best fits your content, but ensuring clarity and accessibility for participants is key.  

## Recommended Folder Structure

While presenters are free to organize their materials, we **recommend** the following structure for clarity:


```
AI-Unlocked-Workshop-2025/
├── README.md                       # Guidelines for presenters
├── AI-Unlocked-workshop-agenda.pdf # Workshop schedule
├── track1-beginner/                # Beginner Track Materials
│   ├── 01-introduction-to-ai/          
│   │   ├── slides.pdf              # Presentation slides by Jason Armbruster (University of Colorado-Boulder)
│   │   ├── workshop-notes.md       # Summary notes
│   │   ├── code/                   # Code files
│   │   │   ├── example1.py
│   │   │   ├── example2.py
│   │   ├── notebooks/              # Jupyter Notebooks
│   │   │   ├── intro_to_ai.ipynb
│   ├── 02-computational-resources/
│   │   ├── slides.pdf              # Presentation by Dave Hart (NCAR)
│   │   ├── workshop-notes.md
│   │   ├── setup-instructions.md   # How to access resources
│   ├── 03-overview-of-ai-tools/
│   │   ├── slides.pdf              # Presentation by Gil Speyer (Arizona State University)
│   │   ├── workshop-notes.md
│   ├── 04-how-to-use-hpc/
│   │   ├── slides.pdf           # Presentation by Mary Thomas (San Diego Supercomputing Center)
│   │   ├── workshop-notes.md
│   │   ├── code/
│   ├── 05-submitting-ai-jobs/
│   │   ├── slides.pdf           # Presentation by Mary Thomas (San Diego Supercomputing Center)
│   │   ├── workshop-notes.md
│   │   ├── code/
│   ├── ... (more sessions) ...
│
├── track2-advanced/             # Advanced Track Materials
│   ├── 01-introduction-to-pytorch/ 
│   │   ├── slides.pdf           # Presentation by Lonnie Crosby (University of Tennessee-Knoxville)
│   │   ├── workshop-notes.md
│   │   ├── code/
│   │   ├── notebooks/
│   ├── 02-ai-tool-lightning-talks/
│   │   ├── slides.pdf           # Talks by Cerebras, Databricks, Google, Microsoft, SambaNova, Cloudbank
│   ├── 03-aws-tools-showcase/
│   │   ├── slides.pdf           # Presentation by Jack Fenwick (Amazon Web Services)
│   │   ├── workshop-notes.md
│   ├── 04-introduction-to-tensorflow/
│   │   ├── slides.pdf           # Presentation by Mahidhar Tatineni (San Diego Supercomputing Center)
│   │   ├── workshop-notes.md
│   ├── 05-ai-using-llms/
│   │   ├── slides.pdf           # Presentation by Danny Havert (Indiana University)
│   │   ├── workshop-notes.md
│   ├── 06-deep-learning-vs-machine-learning/
│   │   ├── slides.pdf           # Presentation by Paola A. Buitrago (Pittsburgh Supercomputing Center)
│   │   ├── workshop-notes.md
│   ├── ... (more sessions) ...
│
├── shared-resources/             # General documents for all attendees
│   ├── how-to-access-hpc.md       # Instructions for accessing Delta/Expanse
│   ├── software-requirements.md   # Python, TensorFlow, PyTorch versions, etc.
│   ├── troubleshooting.md         # Common issues and solutions
│
├── backup-materials/              # Backup of critical files
│   ├── all-slides.zip
│   ├── all-notebooks.zip

```

## How to Use This Structure
- Keep files organized within your track and session.
- Use clear, meaningful filenames.
- Include setup instructions for hands-on exercises.


### **How to Upload Your Files**  
#### **Option 1: Upload via GitHub Web Interface**
1. Navigate to your track folder and session subfolder.  
2. Click `Add file > Upload files`.  
3. Drag and drop your files or select them from your system.  
4. Click `Commit changes`.  

#### **Option 2: Upload via Git (Recommended for multiple files)**
1. Clone the repository:  
   ```bash
   git clone https://github.com/ACCESS/AI-Unlocked-Workshop-2025.git
   cd AI-Unlocked-Workshop-2025
2. Navigate to your session folder and copy your materials there.
3. Add and commit your files:
   ```bash
   git add track1-beginner/01-intro-to-ai/*
   git commit -m "Added workshop materials for Intro to AI"
   git push origin main

#### **Important Guidelines

Ensure your materials are easy to navigate – well-named files help participants find what they need quickly.

Provide setup instructions for running your content, particularly if it requires a specific environment.

Include backup materials (PDFs, notebooks, and code) in case of network issues.

Use Markdown (.md) files where possible for clarity and easy readability.



