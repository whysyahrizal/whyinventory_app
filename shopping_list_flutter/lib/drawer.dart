import 'package:flutter/material.dart';
import 'package:shopping_list/menu.dart';

import 'add_item.dart';

void _navigateToAddItemPage(BuildContext context) {
  Navigator.push(
    context,
    MaterialPageRoute(builder: (context) => const AddItemPage()),
  );
}

void _navigateToHomePage(BuildContext context) {
  Navigator.push(
    context,
    MaterialPageRoute(builder: (context) => MyHomePage()),
  );
}

class MyAppDrawer extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: ListView(
        padding: EdgeInsets.zero,
        children: [
          const DrawerHeader(
            decoration: BoxDecoration(
              color: Colors.indigo,
            ),
            child: Text('Inventory App'),
          ),
          ListTile(
            title: const Text('Halaman Utama'),
            onTap: () {
              Navigator.pop(context);
              _navigateToHomePage(context);
            },
          ),
          ListTile(
            title: const Text('Tambah Item'),
            onTap: () {
              Navigator.pop(context);
              _navigateToAddItemPage(context);
            },
          ),
        ],
      ),
    );
  }
}
