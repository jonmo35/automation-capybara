feature "Wishlist" do
  before do
    visit_home_pg
    visit_signIn_signUp_pg
    expect(page).to have_content("Login")
    login = ::LoginHelper::LoginUser.new
    login.login_form(
      CustomerEmail: "rtassessment@gmail.com",
      CustomerPassword: "!f33db@ck!",
    ).login_button

    expect(find(class: "page-title")).to have_text("My Account")
    expect(current_url).to eq "https://www.gouletpens.com/account"
  end

  describe "Add product to wishlist" do
    it "verify product is in users wishlist" do
      visit "https://www.gouletpens.com/collections/3-oysters/products/3-oysters-delicious-purple-gray-38ml-bottled-ink?variant=12852333051947"
      sleep 5
      find(id: "wishlist_icon").click
      find(class: "header__account-nav-link--wishlist").click
      expect(page).not_to have_selector("#empty-wishlist")
      within("#container wishlistbodycontainer") do
        expect(find('a[href"products/3-oysters-delicious-purple-gray-38ml-bottled-ink?variant=12852333051947"]')).to have_text("3 Oysters Delicious Purple Gray - 38ml Bottled Ink")
      end
      find(class: "clearall").click
    end
  end
end
