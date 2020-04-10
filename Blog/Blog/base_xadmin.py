#!/user/bin/env python
# 每天都要有好心情


class BaseOwnerAdmin:

    exclude = ('owner', )

    def get_list_queryset(self):
        request = self.request
        qs = super().get_list_queryset()
        return qs.filter(owner=request.user)

    def save_models(self):
        self.new_obj.owner = self.request.user
        return super().save_model()
