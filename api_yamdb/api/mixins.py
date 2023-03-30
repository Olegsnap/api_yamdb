from rest_framework import viewsets, mixins


class ListRetrieveCreateDestroyViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    Кастомный вьюсет (миксин)
    Ограничиваает взаимодействие
    """

    pass
