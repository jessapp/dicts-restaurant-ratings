# your code goes here

import sys

#from random import choice


def get_ratings(filename):
    """Print out restaurant names and ratings from file."""

    # Reads ratings data from file into dictionary
    ratings = read_ratings_from_file(filename)
    
    while True:
        print "If you'd like to see the restaurant ratings, press 1."
        print "If you'd like to rate a new restaurant, press 2."
        print "If you want update a restaurant's rating, press 3"
        print "If you'd like to quit, press 4.\n"

        selection = raw_input("> ")

        print 

        if selection == "1":
            print_ratings(ratings)

        elif selection == "2":
            # Collect information from user on a restaurant rating
            new_restaurant = raw_input("Please input a restaurant: ")
            new_rating = raw_input(
                "Please input a rating for the restaurant (as a digit): ")
            try:
                new_rating = int(new_rating)
                ratings[new_restaurant] = new_rating
            except ValueError:
                print "Invalid input"
                continue
            

            print "Restaurant %s has been updated \n" % (new_restaurant)

        elif selection == "3":
            print_ratings(ratings)

            while True:
                # Ask to update a rating
                print "\nWhich restaurant's rating would you like to update?"
                selected_restaurant = raw_input("> ")

                # Check if restaurant is in dictionary
                if selected_restaurant not in ratings:
                    print "Invalid restaurant. Please try again."
                    continue

                else:
                    updated_rating = raw_input(
                        "What would you like the new rating to be? > ")
                    ratings[selected_restaurant] = int(updated_rating)
                    break

            print "%s is now rated at %s \n" % (
                selected_restaurant, ratings[selected_restaurant]
            )

        elif selection == "4":
            break

        else:
            print "That is not a valid option."


def read_ratings_from_file(filename):
    """Open file and creates dictionary from data.

    Reads lines from file that contain <restaurant name>:<rating>.
    Returns a dictionary with restaurants as keys and ratings as values
    """

    # Opens file
    ratings_file = open(filename)

    # Creates empty dictionary
    ratings = {}

    for restaurant in ratings_file:
        # Strips off "/n" and splits on ":"
        restaurant_name, restaurant_rating = restaurant.rstrip().split(':')
        # Inputs restaurant name and rating into dictionary
        ratings[restaurant_name] = restaurant_rating

    return ratings


def print_ratings(ratings):
    """Print each restaurant and its ratings in the ratings dictionary"""

    # Print out name and rating for all restaurants in ratings dict
    for restaurant, rating in sorted(ratings.items()):
        print "%s is rated at %s" % (restaurant, rating)

    print ""



restaurant_file = sys.argv[1]

get_ratings(restaurant_file)
