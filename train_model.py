{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "64753685-a2f4-4dfe-aa5d-ef82fdd472cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model and vectorizer saved to local files\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "import pickle\n",
    "\n",
    "# Load your dataset\n",
    "df = pd.read_csv('C:\\\\Users\\\\\\'Raakha ALAMUKII\\\\Downloads\\\\RecruterPilot candidate sample input dataset - Sheet1.csv')\n",
    "\n",
    "# Sample a fraction of the data\n",
    "sample_data = df.sample(frac=0.1)\n",
    "\n",
    "# Convert all rows to a single text column\n",
    "sample_data['text'] = sample_data.apply(lambda row: ' '.join([str(x) for x in row.values]), axis=1)\n",
    "\n",
    "# For demonstration, let's create a target variable with more than one class\n",
    "sample_data['target'] = sample_data.index % 2  # This will create a binary target with classes 0 and 1\n",
    "\n",
    "# Ensure there are more than one class in the target\n",
    "if len(sample_data['target'].unique()) < 2:\n",
    "    raise ValueError(\"The dataset contains only one class. Ensure there are at least two classes.\")\n",
    "\n",
    "# Vectorize the text data\n",
    "vectorizer = TfidfVectorizer()\n",
    "X = vectorizer.fit_transform(sample_data['text'])\n",
    "y = sample_data['target']\n",
    "\n",
    "# Train a simple model\n",
    "model = LogisticRegression()\n",
    "model.fit(X, y)\n",
    "\n",
    "# Save vectorizer and model to local files\n",
    "with open('vectorizer.pkl', 'wb') as f:\n",
    "    pickle.dump(vectorizer, f)\n",
    "\n",
    "with open('model.pkl', 'wb') as f:\n",
    "    pickle.dump(model, f)\n",
    "\n",
    "print(\"Model and vectorizer saved to local files\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e02b46e-885d-4830-8e2f-9464917f45f8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ed0871a-26bc-4877-9280-5cf678644cdd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39df6c02-8a17-406f-8a5d-9f4ddb384ba4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
