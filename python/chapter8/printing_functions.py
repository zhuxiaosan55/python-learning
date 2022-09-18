def print_models(unprited_design, completed_models):
    while unprited_design:
        current_model = unprited_design.pop()
        print("printing:"+current_model)
        completed_models.append(current_model)
# return completed_models


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
