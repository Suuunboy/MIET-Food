Feature: Order
  Scenario: Add to cart
    Given Main page
    When I click on добавить в корзину
	Then The брусничка should be in the cart
