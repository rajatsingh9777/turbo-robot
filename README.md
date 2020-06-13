#Project Description
The problem was: 
Write REST API in any tech stack of your choice for the following:

A movie actor wants to make the max. money by picking the right movies in a given year.


Rules:

    Consider that the actor gets a fixed amount of 1 Crore for each movie that he does, irrespective of the duration of the money. 

    Movies have a contract where the actor is not allowed to work on other movies whose date conflicts with the selected movies date. For example if the actor have selected a movie from 10th Jan to 20th Jan (both dates inclusive) then actor can’t select any movies which has a start or end date between 10th to 20th Jan.

    Actor is not worried about optimization of less work and more money. His aim is to get the max. money even if he has to work for all the days of the year.



Design a REST API where actor can submit the data containing the list of movies with movie name, start date and end date and the API should return the total amount that he can make along with the final list of movies to select.

Soluton: 
I use Django Rest API where actor can load his data in JSON format.
steps:
1. Sorting the given input 
2. Use Activity  Selection Algorithm to select the given input and find out the output.
3. Use filter to set the year 2020 for an Actor.
 Note* This code will work in MySQL . I used distinct function to remove the repeat dates but by default database of djnago will not allow to add distinct funtion on  a single field.
