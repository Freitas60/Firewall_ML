import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# 1. Nomes das colunas (O NSL-KDD original não as traz)
cols = ["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins","logged_in","num_compromised","root_shell","su_attempted","num_root","num_file_creations","num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login","count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate","label","difficulty"]

# 2. Carregar os dados
print("A carregar dataset...")
df = pd.read_csv('traffic_data.csv', names=cols)

# 3. Limpeza Rápida: Converter texto em números
# O modelo não entende "tcp" ou "private", então usamos o LabelEncoder
le = LabelEncoder()
for col in ['protocol_type', 'service', 'flag']:
    df[col] = le.fit_transform(df[col])

# Transformar a 'label': 'normal' vira 0, qualquer outra coisa vira 1 (ataque)
df['label'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)

# Remover colunas desnecessárias
X = df.drop(['label', 'difficulty'], axis=1)
y = df['label']

# 4. Dividir em Treino (70%) e Teste (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 5. Treinar o modelo
print("A treinar a inteligência da firewall... (isto pode demorar uns segundos)")
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# 6. Avaliar
y_pred = model.predict(X_test)
print("\n[ RESULTADOS DA TUA FIREWALL INTELIGENTE ]")
print(classification_report(y_test, y_pred))
