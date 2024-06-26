class GymMembership:
    def __init__(self, name, base_cost, additional_features=None):
        self.name = name
        self.base_cost = base_cost
        self.additional_features = additional_features if additional_features else {}
        self.selected_features = []

    def add_feature(self, feature_name):
        if feature_name in self.additional_features:
            self.selected_features.append(feature_name)
        else:
            raise ValueError(f"Feature {feature_name} is not available for {self.name} membership.")

    def calculate_cost(self):
        total_cost = self.base_cost
        for feature in self.selected_features:
            total_cost += self.additional_features[feature]
        return total_cost
class Gym:
    def __init__(self):
        self.memberships = {}
        self.group_discount = 0.10
        self.special_discounts = [
            (200, 20),
            (400, 50)
        ]
        self.premium_surcharge = 0.15

    def add_membership(self, membership):
        self.memberships[membership.name] = membership

    def display_memberships(self):
        for membership in self.memberships.values():
            print(f"Membership: {membership.name}, Base Cost: ${membership.base_cost}")
            for feature, cost in membership.additional_features.items():
                print(f"  - Feature: {feature}, Cost: ${cost}")

    def select_membership(self, membership_name):
        if membership_name in self.memberships:
            return self.memberships[membership_name]
        else:
            raise ValueError(f"Membership {membership_name} is not available.")

    def calculate_total_cost(self, membership, num_members=1):
        base_cost = membership.calculate_cost()
        total_cost = base_cost * num_members

        if num_members >= 2:
            total_cost -= total_cost * self.group_discount
            print(f"Group discount applied: {self.group_discount * 100}%")

        for threshold, discount in self.special_discounts:
            if total_cost > threshold:
                total_cost -= discount
                print(f"Special discount of ${discount} applied for total cost over ${threshold}")

        return total_cost

    def confirm_membership(self, membership, num_members=1):
        total_cost = self.calculate_total_cost(membership, num_members)
        print(f"Membership: {membership.name}")
        print(f"Base Cost: ${membership.base_cost}")
        print(f"Additional Features: {', '.join(membership.selected_features)}")
        print(f"Total Cost: ${total_cost}")
        confirmation = input("Do you want to confirm this membership? (yes/no): ").lower()
        if confirmation == 'yes':
            return total_cost
        else:
            return -1
        


def main():
    gym = Gym()
    additional_features = {"WiFi": 10, "Personal Trainer": 50}
    basic_membership = GymMembership("Basic", 100, additional_features)
    premium_membership = GymMembership("Premium", 200)
    family_membership = GymMembership("Family", 300)
    gym.add_membership(basic_membership)
    gym.add_membership(premium_membership)
    gym.add_membership(family_membership)

    while True:
        print("\nAvailable Memberships:")
        memberships_list = list(gym.memberships.values())
        for i, membership in enumerate(memberships_list, start=1):
            print(f"{i}.  {membership.name} - Base Cost: ${membership.base_cost}")
        
        print("\nREMEMBER!!! If two or more members sign up for the same membership plan together, apply a 10 percent discount on the total membership cost")

      
        try:
            membership_selection = int(input("Select a membership plan: ")) - 1
            print (membership_selection)
            if membership_selection < 0 or membership_selection >= len(memberships_list):
                raise ValueError("Invalid selection. Please select a valid number.")
            membership = memberships_list[membership_selection]
            print(membership.name)
            num_members = int(input("Enter the number of members to subscribe: "))

            while True:
                print("\nAvailable Features:")
                for feature in membership.additional_features:
                    print(f"  - {feature}: ${membership.additional_features[feature]}")
                
                feature_name = input("Add a feature (or 'done' to finish): ")
                if feature_name.lower() == 'done':
                    break
                try:
                    membership.add_feature(feature_name)
                except ValueError as e:
                    print(e)

            
            total_cost = gym.confirm_membership(membership, num_members)
            if total_cost != -1:
                print(f"Membership confirmed. Total cost: ${total_cost}")
            else:
                print("Membership not confirmed.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()