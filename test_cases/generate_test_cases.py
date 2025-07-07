sample_tags = [
    "AI", "E-commerce", "Real Estate", "React", "FinTech", "Node JS", "Marketing Automation",
    "Healthcare", "Live Streaming", "Social Media", "XR", "Generative AI", "Mobile App", "VueJS", "Shopify"
]

sample_industries = [
    "Sales & Marketing", "Insurance", "Real Estate", "Art", "Retail", "Education", "Logistics", "CRM"
]

sample_features = [
    "fraud detection", "personalization", "recommendation systems", "chatbot", "dynamic pricing",
    "predictive analytics", "inventory management", "customer engagement", "route optimization"
]

questions = []

for i in range(1, 10):
    if i % 3 == 0:
        questions.append(f"Show me projects related to {sample_tags[i % len(sample_tags)]}")
    elif i % 3 == 1:
        questions.append(f"Which projects are in the {sample_industries[i % len(sample_industries)]} industry?")
    else:
        questions.append(f"Any projects that include {sample_features[i % len(sample_features)]}?")

with open("test_queries.txt", "w") as f:
    for q in questions:
        f.write(q + "\n")
