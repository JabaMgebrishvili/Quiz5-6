# 1. (L12 – 2 ქულა) გამოიყენეთ ერთ ცვლადიანი რეგრესიის მოდელი (Simple linear Regression). გამოთვალეთ
# მოდელის ეფექტურობა და შეამოწმეთ ახალ მონაცემზე რა შედეგს მოგცემთ.

# შემოვიტანოთ აუცილებელი ბიბლიოთეკები და ჩავტვირთოთ პირველი DataFrame
import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# df1 - Student Study Hours.csv - https://www.kaggle.com/datasets/himanshunakrani/student-study-hours
df1 = pd.read_csv('/Student Study Hours.csv')
df1

# მონაცემების ვიზუალიზაცია scatter-ის მეშვეობით
plt.scatter(df1['Hours'], df1['Scores'])
plt.title('Hours vs Scores')
plt.xlabel('Hours')
plt.ylabel('Scores')
plt.show()

# დავყოთთ მონაცემები სატრენინგო და სატესტო ნაწილებად

y = df1['Scores']
X = df1[['Hours']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# მოდელის დატრენინგება LinearRegression()-ის გამოყენებით
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# coefficient-ის and intercept-ის გამოთვლა
coefficient = regressor.coef_[0]
intercept = regressor.intercept_

print(f"Coefficient: {coefficient}")
print(f"Intercept: {intercept}")

# პროგნოზის გაკეთება
y_pred = regressor.predict(X_test)
y_pred

# მოდელის შეფასება
r2 = r2_score(y_test, y_pred)

print(f"R^2 Score: {r2}")

# რეგრესიის ხაზის ვიზუალიზაცია გრაფიკზე
plt.scatter(X, y, color='blue')
plt.plot(X, regressor.predict(X), color='red')
plt.title('Hours vs Scores')
plt.xlabel('Hours')
plt.ylabel('Scores')
plt.show()



# 2. (L12 – 2 ქულა) გამოიყენეთ მრავალ ცვლადიანი რეგრესიის მოდელი (Multiple linear Regression). გამოთვალეთ
# მოდელის ეფექტურობა და შეამოწმეთ ახალ მონაცემზე რა შედეგს მოგცემთ.

# df2 - Real estate.csv - https://www.kaggle.com/datasets/quantbruce/real-estate-price-prediction
df2 = pd.read_csv('/Real estate.csv')
df2

df2.info()

# დავყოთ სვეტები დამოკიდებულ და დამოუკიდებელ ცვლადებად
X = df2.drop(columns=['No', 'Y house price of unit area'])

# სამიზნე სვეტი - 'Y house price of unit area' (Y)
y = df2['Y house price of unit area']

# 80% მონაცემებისა გამოიყენება სატრენინგოდ და 20% კი სატესტოდ
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# მოდელის დათრენინგება
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# coefficients და intercept-ის გამოთვლა
coefficients = regressor.coef_
intercept = regressor.intercept_

print("Coefficients:", coefficients)
print("Intercept:", intercept)

# პროგნოზების გაკეთება
y_pred = regressor.predict(X_test)

# მოდელის შეფასება
# R^2 ქულა მიუთითებს იმაზე, თუ რამდენად კარგად პროგნოზირებს მოდელი შედეგს
r2 = r2_score(y_test, y_pred)
print(f"R^2 Score: {r2}")

# ვიზუალური შედარება რეალურ და პროგნოზირებულ ფასებს შორის
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted Prices')
plt.show()

# Heatmap კორელაციების ვიზუალიზაციისათვის
import seaborn as sns

plt.figure(figsize=(10, 8))
sns.heatmap(df2.corr(), annot=True)
plt.title('Heatmap of Feature Correlations')
plt.show()



# 3. (L13 – 3 ქულა) გამოიყენეთ გადაწყვეტილების ხის რეგრესიის მოდელი ერთ ცვლადზე ან რამდენიმე ცვლადზე
# დამოკიდებულებით. გამოთვალეთ მოდელის ეფექტურობა და შეამოწმეთ ახალ მონაცემზე რა შედეგს
# მოგცემთ.

# df3 - cardekho_data.csv - https://raw.githubusercontent.com/RimjimRazdan/cars_price_prediction/master/car%20data.csv
df3 = pd.read_csv('/cardekho_data.csv')
df3

df3.info()

# საჭირო ბიბლიოთეკებისა და ფუნქციების იმპორტი
from sklearn.tree import DecisionTreeRegressor, export_graphviz, plot_tree
from sklearn.preprocessing import LabelEncoder

# მონაცემების დამუშავება/მომზზადება
# კატეგორიული მნიშვნელობების ენქოდინგი LabelEncoder-ის დახმარებით
label_encoder = LabelEncoder()
df3['Fuel_Type'] = label_encoder.fit_transform(df3['Fuel_Type'])
df3['Seller_Type'] = label_encoder.fit_transform(df3['Seller_Type'])
df3['Transmission'] = label_encoder.fit_transform(df3['Transmission'])

df3.head()

# მონაცემების დაყოფა სატრენონგოდ და სატესტოდ

y = df3['Selling_Price']
X = df3.drop(columns=['Car_Name', 'Selling_Price'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the decision tree regression model
# DecisionTreeRegressor მოდელის შექმან და დატრენინგება შესაბამის სატრენინგო მონაცემებზე
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train, y_train)

# უკვე დატრენინგებული მოდელის გამოყენება ფასის პროგნოზირებისათვის
y_pred = regressor.predict(X_test)

# მოდელის შემოწმება
r2 = r2_score(y_test, y_pred)
print(f"R^2 Score: {r2}")

# გადაწყვეტილების ხის ვიზუალიზაცია
plt.figure(figsize=(20, 10))
plot_tree(regressor, feature_names=X.columns, filled=True)
plt.title('Decision Tree Visualization')
plt.show()

# გადაწყვეტილების ხის .dot ფაილად ექსპორტირება უკეთესად აღსაქმელად (http://www.webgraphviz.com/)
export_graphviz(regressor, out_file='decision_tree.dot', feature_names=X.columns, filled=True)



# 4. (L14 – 3 ქულა) გამოიყენეთ ლოგისტიკური რეგრესიის მოდელი. გამოთვალეთ მოდელის ეფექტურობა და
# შეამოწმეთ ახალ მონაცემზე რა შედეგს მოგცემთ.

# df4 - framingham - logistic to predict heart disease.csv - https://www.kaggle.com/datasets/dileep070/heart-disease-prediction-using-logistic-regression
df4 = pd.read_csv('/framingham - logistic to predict heart disease.csv').head(1000)
df4

df4.info()

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# შევავსოთ გამოტოვებული მნიშვნელობები მედიანით
df4 = df4.fillna(df4.median())

y = df4['TenYearCHD']
X = df4.drop(columns=['TenYearCHD'])

# Heatmap კორელაციების ვიზუალიზაციისათვის
plt.figure(figsize=(10, 8))
sns.heatmap(df4.corr())
plt.title('Heatmap of Feature Correlations')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# ლოგისტიკური რეგრესიის მოდელის დათრენინგება
logistic_regressor = LogisticRegression(max_iter=1000)
logistic_regressor.fit(X_train, y_train)

# პროგნოზის გაკეთება
y_pred = logistic_regressor.predict(X_test)

# მოდელის შეფასება, სიზუსტის ქულა
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy Score: {accuracy}")

# კლასიფიკაციის რეპორტი უფრო დაწვრილებით
print(classification_report(y_test, y_pred))

# Confusion Matrix უკეთესი ვიზუალიზაციისთვის
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()



# 5. (L13 – 4 ქულა) გამოიყენეთ გადაწყვეტილების ხის კლასიფიკაციის მოდელი ერთ ცვლადზე ან რამდენიმე
# ცვლადზე დამოკიდებულებით. გამოთვალეთ მოდელის ეფექტურობა და შეამოწმეთ ახალ მონაცემზე რა
# შედეგს მოგცემთ.

from sklearn.tree import DecisionTreeClassifier

# გადაწყვეტილების ხის კლასიფიკაციის მოდელიის ასაგებად გამოვიყენოთ ისევ df4
classifier = DecisionTreeClassifier(random_state=0)
classifier.fit(X_train, y_train)

# პროგნოზის გაკეთება და სიზუსტის ქულის გამოთვლა
y_pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy Score: {accuracy}")

# გადაწყვეტილების ხის ვიზუალიზაცია
plt.figure(figsize=(20, 10))
plot_tree(classifier, feature_names=X.columns, filled=True)
plt.title('Decision Tree Visualization')
plt.show()

# გადაწყვეტილების ხის .dot ფორმატად ექსპორტი და შენახვა
export_graphviz(classifier, out_file='decisiontree2.dot', feature_names=X.columns, filled=True)
