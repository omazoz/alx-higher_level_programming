#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *curr, *check;

	if (list == NULL || list->next_node == NULL)
		return (0);
	curr = list;
	check = curr->next_node;

	while (curr != NULL && check->next_node != NULL
		&& check->next_node->next_node != NULL)
	{
		if (curr == check)
			return (1);
		curr = curr->next_node;
		check = check->next_node->next_node;
	}
	return (0);
}
