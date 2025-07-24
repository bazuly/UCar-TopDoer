class CreateReviewException(Exception):
    detail = "Failed to create review"


class GetReviewsException(Exception):
    detail = "Failed to get reviews"
