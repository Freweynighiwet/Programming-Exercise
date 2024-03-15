class MinitermFragmentGenerator:
    def __init__(self, predicates):
        self.predicates = predicates

    def generate_fragments(self):
        fragments = []
        for predicate in self.predicates:
            fragment = []
            for key, value in predicate.items():
                fragment.append(f"{key}={value}")
            fragments.append(' AND '.join(fragment))
        return fragments

# Example usage:
predicates = [
    {"age": ">= 18", "gender": "Male"},
    {"salary": "<= 50000", "department": "IT"}
]
generator = MinitermFragmentGenerator(predicates)
fragments = generator.generate_fragments()
for fragment in fragments:
    print(fragment)



