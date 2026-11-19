from django.utils.translation import get_language


class TranslatableModelMixin:
    def get_translated_field(self, field_name, language=None):
        """
            Returns the translated value of a field.

            Example:
                get_translated_field("name") -> name_en | name_es

            Note: Since this requires model to set up properties, 
            we can't directly filter by the property itself 
            
            order_by(name) won't work, it requires name_en or name_es
        """

        if language is None:
            language = get_language()

        language = language.split("-")[0] # We just need en|es, not regional variations like "en-us" or "es-ar"

        translated_field = f"{field_name}_{language}"

        if not hasattr(self, translated_field):
            raise AttributeError(f"Translation field {field_name} does not exist for {self.__class__.__name__}")

        return getattr(self, translated_field)