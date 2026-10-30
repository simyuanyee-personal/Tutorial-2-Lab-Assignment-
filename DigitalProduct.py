from Product import Product


class DigitalProduct(Product):
    """A product delivered electronically (e.g. a download link).

    A digital product IS-A product. It has a download size instead of a
    weight, and deliberately does NOT implement CanBeShipped.
    """

    PRODUCT_TYPE = "digital"

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        if download_size < 0:
            raise ValueError("Download size cannot be negative.")
        self.__download_size = download_size  # megabytes

    def get_download_size(self):
        return self.__download_size

    def display_information(self):
        """Common information from Product, plus this product's download size."""
        super().display_information()
        print(f"    Type: Digital | Download size: {self.__download_size:.2f} MB")

    def get_fulfilment_info(self):
        return "Digital product - delivered electronically via a download link."

    def to_dict(self):
        data = super().to_dict()
        data["download_size"] = self.__download_size
        return data

    @classmethod
    def from_dict(cls, data):
        """Rebuild a DigitalProduct from a saved dictionary."""
        return cls(data["id"], data["name"], data["price"], data["stock"],
                   data["download_size"])