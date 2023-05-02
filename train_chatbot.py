import aiml

BRAIN_FILE = "brain.dump"
AIML_FILES = ["academics.aiml", "hi.aiml", "result.aiml", "std-startup.aiml", "admission.aiml", "department.aiml"]

# Initialize the chatbot and load the AIML files
kernel = aiml.Kernel()
kernel.bootstrap(learnFiles=AIML_FILES)

# Save the chatbot's knowledge to a new brain file
kernel.saveBrain(BRAIN_FILE)
