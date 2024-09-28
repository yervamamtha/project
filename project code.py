class CodeArea:
    def __init__(self, code_area_id, description, initial_debt, refactor_cost):
        self.code_area_id = code_area_id
        self.description = description
        self.initial_debt = initial_debt
        self.refactor_cost = refactor_cost
        self.debt_interest = 0

class TechnicalDebtTracker:
    def __init__(self):
        self.code_areas = {}

    def add_or_update_code_area(self, code_area_id, description, initial_debt, refactor_cost):
        """Create or update a code area with technical debt details."""
        self.code_areas[code_area_id] = CodeArea(code_area_id, description, initial_debt, refactor_cost)

    def estimate_debt_interest(self, code_area_id, months_passing, interest_rate=0.05):
        """Estimate additional debt accrued by not addressing technical debt."""
        if code_area_id in self.code_areas:
            area = self.code_areas[code_area_id]
            area.debt_interest = area.initial_debt * ((1 + interest_rate) ** months_passing - 1)
            return area.debt_interest
        else:
            return "Code area not found."

    def prioritize_refactoring(self):
        """Prioritize code areas for refactoring based on debt-to-refactor ratio."""
        priorities = []
        for area_id, area in self.code_areas.items():
            debt_to_refactor_ratio = (area.initial_debt + area.debt_interest) / area.refactor_cost
            priorities.append((area_id, debt_to_refactor_ratio))
        
        # Sort areas by their debt-to-refactor ratio in descending order
        priorities.sort(key=lambda x: x[1], reverse=True)
        return priorities

# Example usage
if __name__ == "__main__":
    tracker = TechnicalDebtTracker()

    # Adding code areas
    tracker.add_or_update_code_area("area1", "User Authentication Module", 5000, 20000)
    tracker.add_or_update_code_area("area2", "Payment Processing Module", 3000, 15000)

    # Estimating debt interest after 6 months
    interest_area1 = tracker.estimate_debt_interest("area1", 6)
    interest_area2 = tracker.estimate_debt_interest("area2", 6)

    print(f"Debt interest for area1 after 6 months: ${interest_area1:.2f}")
    print(f"Debt interest for area2 after 6 months: ${interest_area2:.2f}")

    # Prioritizing refactoring
    priorities = tracker.prioritize_refactoring()
    print("Refactoring priorities (area_id, debt-to-refactor ratio):")
    for area_id, ratio in priorities:
        print(f"{area_id}: {ratio:.2f}")
