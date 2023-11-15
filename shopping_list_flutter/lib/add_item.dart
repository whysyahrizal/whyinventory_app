import 'package:flutter/material.dart';
import 'package:shopping_list/drawer.dart';

class AddItemPage extends StatelessWidget {
  const AddItemPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Tambah Item Baru'),
      ),
      drawer: MyAppDrawer(),
      body: AddItemForm(),
    );
  }
}

class AddItemForm extends StatefulWidget {
  @override
  _AddItemFormState createState() => _AddItemFormState();
}

class Product {
  final String name;
  final int amount;
  final String description;

  Product(this.name, this.amount, this.description);
}

class _AddItemFormState extends State<AddItemForm> {
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();
  TextEditingController _nameController = TextEditingController();
  TextEditingController _amountController = TextEditingController();
  TextEditingController _descriptionController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(16.0),
      child: Form(
        key: _formKey,
        child: Column(
          children: [
            TextFormField(
              controller: _nameController,
              decoration: InputDecoration(labelText: 'Name'),
              validator: (value) {
                if (value == null || value.isEmpty) {
                  return 'Name cannot be empty';
                }

                if (value is! String) {
                  return "Name must be a string";
                }
                return null;
              },
            ),
            TextFormField(
              controller: _amountController,
              decoration: InputDecoration(labelText: 'Amount'),
              validator: (value) {
                if (value == null || value.isEmpty) {
                  return 'Amount cannot be empty';
                }

                if (int.tryParse(value!) == null) {
                  return 'Amount must be an integer';
                }

                return null;
              },
            ),
            TextFormField(
              controller: _descriptionController,
              decoration: InputDecoration(labelText: 'Description'),
              validator: (value) {
                if (value == null || value.isEmpty) {
                  return 'Description cannot be empty';
                }

                if (value is! String) {
                  return "Description must be a string";
                }
                return null;
              },
            ),
            SizedBox(height: 16),
            ElevatedButton(
              onPressed: () {
                if (_formKey.currentState!.validate()) {
                  _showConfirmationPopup();
                }
              },
              child: Text('Save'),
            ),
          ],
        ),
      ),
    );
  }

  void _showConfirmationPopup() {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Item Berhasil Ditambahkan!'),
          content: Text(
            'Name: ${_nameController.text}\nAmount: ${_amountController.text}\nDescription: ${_descriptionController.text}',
          ),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: Text('OK'),
            ),
          ],
        );
      },
    );
  }
}
