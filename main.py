
class GymMembership:
    def __init__(self, name, base_cost, additional_features=None):
        self.name = name
        self.base_cost = base_cost
        self.additional_features = additional_features if additional_features else {}
        self.selected_features = []

    def add_feature(self, feature_name):
        if feature_name in self.additional_features:
            self.selected_features.append(feature_name)
            print("\n-----------------------------------------------------\n" +
                f"Adding {feature_name} feature to your membership...\n" +
                "-----------------------------------------------------\n ")
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
    basic_features = {"Group Classes": 25, "Crossfit Sessions": 10}
    premium_features = {"Personal Trainer": 40, "Sauna": 10, "Nutrition Plan": 20}
    family_features = {"Tennis Court": 10, "Group Classes": 15}

    basic_membership = GymMembership("Basic", 60, basic_features)
    premium_membership = GymMembership("Premium", 80, premium_features)
    family_membership = GymMembership("Family", 100, family_features)

    gym.add_membership(basic_membership)
    gym.add_membership(premium_membership)
    gym.add_membership(family_membership)

    while True:
        print("\n -----------------WELCOME TO YOUR FAVOURITE GYM-------------------\n" +"\nAvailable Memberships:")
        memberships_list = list(gym.memberships.values())
        for i, membership in enumerate(memberships_list, start=1):
            print(f"{i}.  {membership.name} - Base Cost: ${membership.base_cost}")

        print("\n ------------------------ATENTION!!------------------------------------\n" +
            "\n If two or more members sign up for the same membership plan together, \n apply a 10 percent discount on the total membership cost\n" +
            "\n ------------------------------------------------------------------------\n")
      
        try:
            membership_selection = int(input("Select a membership plan: ")) - 1
            if membership_selection < 0 or membership_selection >= len(memberships_list):
                raise ValueError("Invalid selection. Please select a valid number.")
            membership = memberships_list[membership_selection]
            print(f"\nYou have choosen {membership.name} Plan for your membership." )
            num_members = int(input("\nEnter the number of members to subscribe: "))

            while True:
                print("\nAvailable Features:")
                features_list = [feature for feature in membership.additional_features.keys() if feature not in membership.selected_features]
                for i, feature in enumerate(features_list, start=1):
                    print(f"{i}. {feature}: ${membership.additional_features[feature]}")
                
                feature_selection = input("\nSelect a feature to add (or 'done' to finish): ")
                if feature_selection.lower() == 'done':
                    break
                else:
                    try:
                        feature_selection = int(feature_selection) - 1
                        if feature_selection < 0 or feature_selection >= len(features_list):
                            raise ValueError("Invalid selection. Please select a valid number.")
                        feature_name = features_list[feature_selection]
                        membership.selected_features.append(feature_name)  # Asumiendo que selected_features es un set
                        print(f"Adding {feature_name} feature to your membership.")
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
