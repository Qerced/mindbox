from pyspark.sql import DataFrame, SparkSession


def get_product_and_category_names(
    products: DataFrame,
    categories: DataFrame,
    product_category: DataFrame
) -> DataFrame:
    return product_category.join(
        products, product_category.product_id == products.id, "outer"
    ).join(
        categories, product_category.category_id == categories.id, "outer"
    ).select(
        products.name, categories.name
    )


if __name__ == "__main__":
    import os
    import sys

    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

    spark: SparkSession = SparkSession.builder.getOrCreate()

    get_product_and_category_names(
        spark.createDataFrame(
            [(1, "product A", 10), (2, "product B", 20), (3, "product C", 30)],
            ["id", "name", "price"]
        ),
        spark.createDataFrame(
            [(1, "category A"), (2, "category B"), (3, "category C")],
            ["id", "name"]
        ),
        spark.createDataFrame(
            [(1, 1), (1, 2), (2, 2)], ["product_id", "category_id"]
        )
    ).show()

    spark.stop()
