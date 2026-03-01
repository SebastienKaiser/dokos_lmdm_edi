# Dokos LMDM - EDI Integration

Application Frappe/ERPNext pour l'intégration EDI (Electronic Data Interchange) dans Dokos LMDM.

## 🎯 Fonctionnalités

- **Interface d'administration** : Configuration centralisée via EDI Settings
- **Navigation intuitive** : Menu EDI dans le sidebar avec sections Flux et Données
- **API whitelisted** : Endpoints sécurisés pour synchronisation externe
- **Auto-synchronization** : Configuration interval pour sync automatique

## 📦 Structure

```
dokos_lmdm_edi/
├── doctype/
│   └── edi_settings/          # Configuration EDI (Single DocType)
├── workspace/
│   └── edi/                   # Navigation workspace EDI
├── dokos_lmdm_edi/
│   └── module_def/            # Enregistrement du module
├── public/js/                 # Scripts client-side
├── api.py                     # API whitelisted
└── hooks.py                   # Configuration de l'app
```

## 🚀 Installation

### 1. Synchroniser l'app sur GitHub

```powershell
# Depuis c:\workspace\dokos_lmdm
.\dokint.ps1 app sync edi --message "Initial EDI app structure"
```

### 2. Installer sur le serveur Dokos

```bash
# Sur le serveur Dokos
cd /path/to/frappe-bench

# Récupérer l'app depuis GitHub
bench get-app dokos_lmdm_edi https://github.com/YOUR_ORG/dokos-lmdm-edi.git

# Installer sur le site dev
bench --site dev.local install-app dokos_lmdm_edi

# Migrer la base de données
bench --site dev.local migrate

# Redémarrer
bench restart
```

### 3. Vérification

1. **Menu EDI** : Vérifier que le lien "EDI" apparaît dans le sidebar
2. **EDI Settings** : Accéder à Administration > EDI Settings
3. **Workspace** : Cliquer sur EDI pour voir le workspace avec sections

## ⚙️ Configuration

### EDI Settings (Administration)

Accessible via : **Administration** > **EDI Settings**

**Champs de configuration :**

| Champ | Type | Description |
|-------|------|-------------|
| Title | Data | Titre de la configuration |
| Description | Text Editor | Description de l'intégration EDI |
| Status | Select | Active / Inactive |
| API Endpoint | Data | URL de l'API EDI externe |
| API Key | Password | Clé d'authentification API |
| Enable Auto Sync | Check | Activer synchronisation automatique |
| Sync Interval | Int | Intervalle en minutes (min: 1) |

**Validation :**
- L'API Endpoint doit commencer par `http://` ou `https://`
- L'intervalle de sync doit être ≥ 1 minute

**Permissions :**
- Accessible uniquement aux **System Manager**

## 🔌 API Endpoints

Tous les endpoints sont whitelisted et accessible via `/api/method/...`

### get_status()

Vérifier que l'app EDI est active.

```python
frappe.call({
    method: "dokos_lmdm_edi.api.get_status",
    callback: function(r) {
        console.log(r.message);
        // {status: "ok", version: "1.0.0", message: "EDI Integration App is running"}
    }
});
```

### get_edi_settings()

Récupérer la configuration EDI courante.

```python
frappe.call({
    method: "dokos_lmdm_edi.api.get_edi_settings",
    callback: function(r) {
        console.log(r.message);
        // {title: "EDI Configuration", status: "Active", ...}
    }
});
```

### update_edi_settings()

Mettre à jour la configuration EDI (System Manager uniquement).

```python
frappe.call({
    method: "dokos_lmdm_edi.api.update_edi_settings",
    args: {
        api_endpoint: "https://edi.example.com/api",
        enable_auto_sync: 1,
        sync_interval: 60
    },
    callback: function(r) {
        console.log(r.message);
        // {status: "success", message: "EDI Settings updated successfully"}
    }
});
```

### sync_edi_data()

Déclencher une synchronisation EDI manuelle.

```python
frappe.call({
    method: "dokos_lmdm_edi.api.sync_edi_data",
    callback: function(r) {
        console.log(r.message);
        // {status: "success", message: "EDI sync completed", synced: 0}
    }
});
```

## 🧪 Tests

### Tests unitaires

```bash
# Sur le serveur Dokos
bench --site dev.local run-tests --app dokos_lmdm_edi

# Tester un DocType spécifique
bench --site dev.local run-tests --doctype "EDI Settings"
```

### Tests manuels

1. **Créer EDI Settings :**
   - Aller dans Administration > EDI Settings
   - Remplir les champs
   - Sauvegarder
   - Vérifier validation (URL, intervalle)

2. **Tester API :**
   ```javascript
   // Depuis la console du navigateur
   frappe.call({
       method: "dokos_lmdm_edi.api.get_status",
       callback: r => console.log(r.message)
   });
   ```

3. **Vérifier Workspace :**
   - Cliquer sur EDI dans le sidebar
   - Vérifier sections : Gestion EDI, Flux EDI, Données EDI
   - Tester le shortcut vers EDI Settings

## 📋 À faire (Prochaines étapes)

### Phase 1 : Structure de base ✅
- [x] EDI Settings (Single DocType)
- [x] EDI Workspace avec navigation
- [x] Module Def registration
- [x] API endpoints de base
- [x] Tests unitaires

### Phase 2 : Flux EDI
- [ ] Créer DocType "Flux EDI" (gestion des flux)
- [ ] Liste des flux entrants/sortants
- [ ] Statut des transmissions
- [ ] Journal des échanges

### Phase 3 : Données EDI
- [ ] Mapping des données (Dokos ↔ EDI)
- [ ] Configuration des formats EDI (EDIFACT, XML, JSON)
- [ ] Validation des messages EDI
- [ ] Transformation des données

### Phase 4 : Automatisation
- [ ] Scheduler pour auto-sync
- [ ] Webhooks pour événements temps réel
- [ ] Notifications (succès/erreur)
- [ ] Retry logic pour échecs

## 🐛 Dépannage

### L'app n'apparaît pas dans la liste

```bash
# Vérifier que l'app est bien installée
bench --site dev.local list-apps

# Si absente, installer
bench --site dev.local install-app dokos_lmdm_edi
```

### Le workspace EDI n'apparaît pas

```bash
# Forcer la reconstruction du workspace
bench --site dev.local rebuild-workspace

# Ou migrer à nouveau
bench --site dev.local migrate
```

### Erreur de permissions

- Vérifier que l'utilisateur a le rôle **System Manager**
- Pour donner le rôle : Setup > Users > [User] > Roles > Cocher "System Manager"

### API endpoint retourne 404

- Vérifier que la méthode est bien whitelisted (`@frappe.whitelist()`)
- Redémarrer bench : `bench restart`
- Vérifier le chemin : `dokos_lmdm_edi.api.get_status`

## 📚 Ressources

- [Frappe Framework Documentation](https://frappeframework.com/docs)
- [ERPNext Developer Guide](https://docs.erpnext.com/docs/user/en/contribution/guidelines)
- [Frappe Workspace Guide](https://frappeframework.com/docs/user/en/desk/workspace)
- [Single DocType Pattern](https://frappeframework.com/docs/user/en/basics/doctypes/single-doctype)

## 📄 Licence

MIT License

## 👥 Auteurs

Développé pour Dokos LMDM
