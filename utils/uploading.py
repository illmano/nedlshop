class ImageUploadHelper:
    FIELD_TO_COMBINE_MAP = {
        'default': {
            'upload_postfix': 'uploads'
        },
        'Product': {
            'field': 'slug',
            'upload_postfix': 'product_images'
        }
    }

    def __init__(self, field_name_to_combine, instance, filename, upload_postfix):
        self.field_name_to_combine = field_name_to_combine
        self.instance = instance
        self.extension = filename.split('.')[-1]
        self.upload_postfix = f"_{upload_postfix}"

    @classmethod
    def get_field_to_combine_and_upload_postfix(cls, klass):
        field_to_combine = cls.FIELD_TO_COMBINE_MAP[klass]['field']
        upload_postfix = cls.FIELD_TO_COMBINE_MAP.get(
            'upload_postfix', cls.FIELD_TO_COMBINE_MAP['default']['upload_postfix']
        )
        return field_to_combine,  upload_postfix
