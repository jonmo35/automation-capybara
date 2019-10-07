module Pages
  def visit_wishList_pg
    click_link("My Wishlist", :href => "/a/wishlist")
    expect(page).to have_content "Wishlist"
  end

  def visit_home_pg
    visit "#{$base_url}"
  end

  def visit_signIn_signUp_pg
    click_link("Sign In / Sign Up", :href => "/account/login")
    expect(current_url).to eq "https://www.gouletpens.com/account/login"
    expect(page).to have_content "Login"
  end
end
