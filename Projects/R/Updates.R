# list all packages where an update is available
old.packages()

# update all available packages
update.packages()

# update, without prompts for permission/clarification
update.packages(ask = FALSE)

# update only a specific package
install.packages("plotly")

# remove only a specific package
remove.packages("plotly")