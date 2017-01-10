# your code goes here

import sys

from random import choice


def get_ratings(file):
    """Prints out restaurant names and ratings from file."""

    # Opens file
    ratings_file = open(file)

    # Creates empty dictionary
    ratings = {}

    for restaurant in ratings_file:
        # Strips off "/n" and splits on ":"
        restaurant_name, restaurant_rating = restaurant.rstrip().split(':')
        # Inputs restaurant name and rating into dictionary
        ratings[restaurant_name] = restaurant_rating

    while True:
        print "If you'd like to see the restaurant ratings, press 1."
        print "If you'd like to rate a new restaurant, press 2."
        print "If you want update a restaurant's rating, press 3"
        print "If you'd like to quit, press 4.\n"

        selection = raw_input("> ")

        print ""

        if selection == "1":
            # Print out name and rating for all restaurants in ratings dict
            for restaurant, rating in sorted(ratings.items()):
                print "%s is rated at %s" % (restaurant, rating)

        elif selection == "2":
            # Collect information from user on a restaurant rating
            new_restaurant = raw_input("Please input a restaurant: ")
            new_rating = raw_input("Please input a rating for the restaurant (as a digit): ")
            new_rating = int(new_rating)
            ratings[new_restaurant] = new_rating

        elif selection == "3":
            # Print out existing ratings
            for restaurant, rating in sorted(ratings.items()):
                print "%s is rated at %s" % (restaurant, rating)

            while True:
                # Ask to update a rating
                print "\nWhich restaurant's rating would you like to update?"
                selected_restaurant = raw_input("> ")

                # Check if restaurant is in dictionary
                if selected_restaurant not in ratings:
                    print "Invalid restaurant. Please try again."
                    continue

                else:
                    updated_rating = raw_input("What would you like the new rating to be? > ")
                    ratings[selected_restaurant] = updated_rating
                    break

            print "%s is now rated at %s \n" % (selected_restaurant, ratings[selected_restaurant])

        elif selection == "4":
            break

        else:
            print "That is not a valid option."


restaurant_file = sys.argv[1]

get_ratings(restaurant_file)
