#include "lists.h"

/**
 *insert_node - Inserts a number into a sorted singly-linked list
 *@head: A pointer the head of the linked list
 *@number: The number to insert
 *
 *Return: NULL in case of failure
 *	a pointer to the new mode
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *the_new;

	the_new = malloc(sizeof(listint_t));
	if (the_new == NULL)
		return (NULL);
	the_new->n = number;

	if (node == NULL || node->n >= number)
	{
		the_new->next = node;
		*head = the_new;
		return (the_new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	the_new->next = node->next;
	node->next = the_new;

	return (the_new);
}



