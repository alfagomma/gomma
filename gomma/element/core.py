#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Element SDK
"""

__author__ = "Davide Pellegrino"
__version__ = "3.1.2"
__date__ = "2022-03-25"

import logging

from gomma.session import Session


class Element(object):
    """
    Element core class .
    """

    def __init__(self, profile_name=None):
        """
        Init Element cls.
        """
        logging.info(f"Init Element SDK -p {profile_name}")
        s = Session(profile_name)
        self.host = s.config.get("agapi_host")
        logging.debug(f"host is {self.host}")
        self.s = s

    # item
    def getItem(self, item_id: int, params: dict = {}):
        """
        Legge un item dal suo id.
        """
        logging.debug(f"Get item {item_id}")
        rq = f"{self.host}/item/{item_id}"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getItems(self, params: dict = {}):
        """
        Prende tutti gli items.
        """
        logging.debug("Getting all the items")
        rq = f"{self.host}/item"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def createItem(self, payload: dict):
        """
        Create new item.
        """
        logging.debug(f"Creating item {payload}")
        rq = f"{self.host}/item"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getItemFromErp(self, erp_id: int, erp_code: str, params: dict = {}):
        """
        Get item from erp.
        """
        logging.debug(f"Search item from erp {erp_id} code {erp_code}.")
        query = {**params, **{"erp": erp_id, "code": erp_code}}
        rq = f"{self.host}/item/findByErp"
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def getItemFromCode(self, item_code: str, params: dict = {}):
        """
        Get item from code
        """
        logging.debug(f"Search item code {item_code}.")
        query = {**params, **{"code": item_code}}
        rq = f"{self.host}/item/findByCode"
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def attachItemErp(self, item_id: int, payload: dict):
        """
        Attach Item Erp references.
        """
        logging.debug(f"Attaching item {item_id} erp with {payload}")
        rq = f"{self.host}/item/{item_id}/erp"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def updateItem(self, item_id: int, payload: dict):
        """
        Update item.
        """
        logging.debug(f"Updating item {item_id} with {payload}")
        rq = f"{self.host}/item/{item_id}"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def patchItem(self, item_id: int, payload: dict):
        """
        Patch know item field.
        """
        logging.debug(f"Patching item {item_id} with {payload}")
        rq = f"{self.host}/item/{item_id}"
        agent = self.s.getAgent()
        r = agent.patch(rq, json=payload)
        return self.s.response(r)

    def ItemAddAttribute(self, item_id: int, payload: dict):
        """
        Create new item attributes.
        """
        logging.debug(f"Creating item {item_id} attributes {payload}")
        rq = f"{self.host}/item/{item_id}/attribute"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def itemPatchAttribute(self, item_id: int, attribute_id: int, payload: dict):
        """
        Patch item attribute.
        """
        logging.debug(f"Patch item {item_id} attribute {attribute_id}-{payload}")
        rq = f"{self.host}/item/{item_id}/attribute/{attribute_id}"
        agent = self.s.getAgent()
        r = agent.patch(rq, json=payload)
        return self.s.response(r)

    def itemRemoveAttribute(self, item_id: int, attribute_id: int):
        """
        Remove item attribute.
        """
        logging.debug(f"Remove item {item_id} attribute {attribute_id}")
        rq = f"{self.host}/item/{item_id}/attribute/{attribute_id}"
        agent = self.s.getAgent()
        r = agent.delete(rq)
        return self.s.response(r)

    def syncItemNorm(self, item_id: int, payload: dict):
        """
        Sync item norm.
        """
        logging.debug(f"Sync item {item_id} norm {payload}")
        rq = f"{self.host}/item/{item_id}/norm"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def itemAddCompetitor(self, item_id: int, payload: dict):
        """attach competitor to the item"""
        logging.debug(f"Add xref item {item_id} {payload}")
        rq = f"{self.host}/item/{item_id}/competitor"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def itemUpdateCompetitor(self, item_id: int, xref_id: int, code: str):
        """update item competitor cross reference"""
        logging.debug(f"Update competitor {xref_id} with code {code}")
        payload = {"code": code}
        rq = f"{self.host}/item/{item_id}/competitor/{xref_id}"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def itemDeleteCompetitor(self, item_id: int, competitor_id: int):
        """Remove item competitor cross reference"""
        logging.debug(f"Removing competitor {competitor_id} xref from item {item_id}")
        rq = f"{self.host}/item/{item_id}/competitor/{competitor_id}"
        agent = self.s.getAgent()
        r = agent.delete(rq)
        return self.s.response(r)

    # attribute
    def createAttribute(self, payload: dict):
        """crea un nuovo attributo"""
        logging.debug(f"Creating new attribute {payload}")
        rq = f"{self.host}/attribute"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getAttributes(self, params: dict = {}):
        """
        Read all attributes.
        """
        logging.debug("Getting all the attributes.")
        rq = f"{self.host}/attribute"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getAttribute(self, attribute_id: int, params: dict = {}):
        """Attribute by id"""
        logging.debug(f"Get attribute {attribute_id}")
        rq = f"{self.host}/attribute/{attribute_id}"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getAttributeByName(self, attribute_name: str, params: dict = {}):
        """Attribute by name"""
        logging.debug(f"Get attribute by name {attribute_name}")
        query = {**params, **{"name": attribute_name}}
        rq = f"{self.host}/attribute/findByName"
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def updateAttribute(self, attribute_id: int, payload: dict):
        """
        Update attribute.
        """
        logging.debug(f"Updating attribute {attribute_id} ...")
        rq = f"{self.host}/attribute/{attribute_id}"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    # attribute
    def createAttributeValue(self, attribute_id: int, payload: dict):
        """Crete new attribute value."""
        logging.debug(f"Creating new attribute value {payload}")
        rq = f"{self.host}/attribute/{attribute_id}/value"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getAttributesValues(self, attribute_id: int, params: dict = {}):
        """
        Read all attribute values.
        """
        logging.debug("Getting all the attribute values.")
        rq = f"{self.host}/attribute/{attribute_id}/value"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getAttributeValue(self, attribute_id: int, value_id: int, params: dict = {}):
        """Attribute value by id"""
        logging.debug(f"Get attribute {attribute_id} value {value_id}")
        rq = f"{self.host}/attribute/{attribute_id}/value/{value_id}"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getAttributeValueByName(
        self, attribute_id: int, value_name: str, params: dict = {}
    ):
        """Attribute by name"""
        logging.debug(f"Get attribute {attribute_id} value by name {value_name}")
        query = {**params, **{"name": value_name}}
        rq = f"{self.host}/attribute/{attribute_id}/value/findByName"
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def updateAttributeValue(self, attribute_id: int, value_id: int, payload: dict):
        """
        Update attribute value.
        """
        logging.debug(f"Updating attribute {attribute_id} value{value_id} ...")
        rq = f"{self.host}/attribute/{attribute_id}/value/{value_id}"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    # application
    def application_list(self, params: dict = {}):
        """
        Read all applications.
        """
        logging.debug("Getting all the applications")
        rq = f"{self.host}/application"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def application_create(self, payload: dict):
        """
        Create new application.
        """
        logging.debug(f"Creating application {payload}")
        rq = f"{self.host}/application"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def application_by_id(self, application_id: int, params: dict = {}):
        """
        Read single application.
        """
        logging.debug(f"Get application {application_id}")
        rq = f"{self.host}/application/{application_id}"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def application_by_name(self, name: str, params: dict = {}):
        """
        Read single application by name.
        """
        logging.debug(f"Get application name {name}")
        rq = f"{self.host}/application/findByName"
        query = {**params, **{"name": name}}
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def application_update(self, application_id: int, payload: dict):
        """
        Update application.
        """
        logging.debug(f"Updating application {application_id} with {payload}")
        rq = f"{self.host}/application/{application_id}"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def application_attach_market(self, application_id: int, market_id: int):
        """
        Attach market to application.
        """
        logging.debug(f"Attaching market {market_id} to application {application_id}.")
        rq = f"{self.host}/application/{application_id}/market"
        payload = {"market_id": market_id}
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def application_detach_market(self, application_id: int, market_id: int):
        """
        Remove application market id.
        """
        logging.debug(f"Remove application {application_id} market {market_id} ...")
        rq = f"{self.host}/application/{application_id}/market/{market_id}"
        agent = self.s.getAgent()
        r = agent.delete(rq)
        return self.s.response(r)

    # family

    def createFamily(self, payload: dict):
        """crea una nuova famiglia"""
        logging.debug(f"Creating new family {payload}")
        rq = f"{self.host}/family"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getFamilies(self, params: dict = {}):
        """
        Prende tutte le famiglie.
        """
        logging.debug(f"Getting all the families with params {params}")
        rq = f"{self.host}/family"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getFamily(self, family_id: int, params: dict = {}):
        """
        Legge la singola famiglia.
        """
        logging.debug(f"Reading family {family_id}")
        rq = f"{self.host}/family/{family_id}"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def updateFamily(self, family_id: int, payload: dict):
        """
        Update family.
        """
        logging.debug(f"Updating family {family_id} with {payload}")
        rq = f"{self.host}/family/{family_id}"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getFamilyFromCode(self, family_code: str, params: dict = {}):
        """Prende famiglia da nome"""
        logging.debug(f"Get family from code {family_code} with {params}")
        query = {**params, **{"code": family_code}}
        rq = f"{self.host}/family/findByCode"
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def getFamilyAttributes(self, family_id: int, params: dict = {}):
        """Read family attributes"""
        logging.debug(f"getFamilyAttributes {family_id} with params {params}")
        rq = f"{self.host}/family/{family_id}/attribute"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def patchFamily(self, family_id: int, payload: dict):
        """
        Patch family data.
        """
        logging.debug(f"Patching family {family_id} with {payload}")
        rq = f"{self.host}/family/{family_id}"
        agent = self.s.getAgent()
        r = agent.patch(rq, json=payload)
        return self.s.response(r)

    def patchFamilyCategory(self, family_id: int, category_id: int):
        """
        Associa categoria a famiglia
        """
        logging.debug(f"Patching family {family_id} with category {category_id}")
        rq = f"{self.host}/family/{family_id}"
        payload = {"category_id": category_id}
        agent = self.s.getAgent()
        r = agent.patch(rq, json=payload)
        return self.s.response(r)

    def updateFamilyCover(self, family_id: int, localFile):
        """
        Aggiorna cover famiglia.
        """
        logging.debug(f"Update family {family_id} cover with file {localFile}")
        rq = f"{self.host}/family/{family_id}/cover"
        fin = open(localFile, "rb")
        files = {"src": fin}
        agent = self.s.getAgent()
        r = agent.post(rq, files=files)
        return self.s.response(r)

    def updateFamilyHq(self, family_id: int, localFile):
        """
        Aggiorna HQ famiglia.
        """
        logging.debug(f"Update family {family_id} hq with file {localFile}")
        rq = f"{self.host}/family/{family_id}/hq"
        fin = open(localFile, "rb")
        files = {"src": fin}
        # files = {'src': ('test.cad', open(filepath, 'rb'), 'image/png')}
        agent = self.s.getAgent()
        r = agent.post(rq, files=files)
        return self.s.response(r)

    def attachFamilyNorm(self, family_id: int, norm_id: int):
        """
        Aggiunge una norma riconosciuta, alla famiglia.
        SUGGEST - USE syncFamilyNorm!
        """
        logging.debug(f"Attaching norm {norm_id} at family {family_id} ...")
        rq = f"{self.host}/family/{family_id}/norm"
        payload = {"norm_id": norm_id}
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def attachFamilyQuality(self, family_id: int, quality_id: int):
        """
        Aggiunge una qualità alla famiglia
        SUGGEST - USE syncFamilyNorm!
        """
        logging.debug(f"Attach quality {quality_id} at family {family_id}")
        rq = f"{self.host}/family/{family_id}/quality"
        payload = {"quality_id": quality_id}
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def attachFamilyFeature(self, family_id: int, feature_id: int, description: str):
        """
        Aggiunge una feature alla famiglia.
        """
        logging.debug(
            f"Attaching feature {feature_id} at family {family_id} with description {description}"
        )
        payload = {"feature_id": feature_id, "description": description}
        rq = f"{self.host}/family/{family_id}/feature"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def attachFamilyAttribute(self, family_id: int, attribute_id: int):
        """
        Add attribute to family.
        """
        logging.debug(f"Attaching attribute {attribute_id} to family {family_id}...")
        rq = f"{self.host}/family/{family_id}/attribute"
        payload = {"attribute_id": attribute_id}
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def updateFamilyAttributePosition(self, family_id: int, positions: list):
        """
        Update family attribute position.
        """
        logging.debug(f"Updating family {family_id} attribute position...")
        rq = f"{self.host}/family/{family_id}/attribute/position"
        payload = {"positions": positions}
        agent = self.s.getAgent()
        r = agent.put(rq, json=payload)
        return self.s.response(r)

    def attachFamilySorting(self, family_id: int, attribute_id: int):
        """
        Add attribute to sorting
        """
        logging.debug(
            f"Attaching attribute {attribute_id} to family {family_id} sorting..."
        )
        rq = f"{self.host}/family/{family_id}/sorting"
        payload = {"attribute_id": attribute_id}
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def updateFamilySortingPosition(self, family_id: int, positions: list):
        """
        Update family sorting position.
        """
        logging.debug(f"Updating family {family_id} sorting position...")
        rq = f"{self.host}/family/{family_id}/sorting/position"
        payload = {"positions": positions}
        agent = self.s.getAgent()
        r = agent.put(rq, json=payload)
        return self.s.response(r)

    # feature
    def createFeature(self, feature_name: str):
        """
        Crea una nuova feature.
        """
        logging.debug(f"Creating new feature with name {feature_name}")
        rq = f"{self.host}/feature"
        payload = {"name": feature_name}
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getFeatureByName(self, feature_name: str, params: dict = {}):
        """
        Prende feature dal nome.
        """
        logging.debug(f"Getting feature by name {feature_name}...")
        query = {**params, **{"name": feature_name}}
        rq = f"{self.host}/feature/findByName"
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    # hub
    def getHubByName(self, hub_name: str):
        """
        Get hub from name
        """
        logging.debug(f"Search hub by name {hub_name}")
        rq = f"{self.host}/hub/findByName?name={hub_name}"
        agent = self.s.getAgent()
        r = agent.get(rq)
        return self.s.response(r)

    def createHub(self, payload: dict):
        """
        Create new hub
        """
        logging.debug(f"Creating new hub {payload}")
        rq = f"{self.host}/hub"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    # category
    def createCategory(self, payload: dict):
        """
        Crea un categoria.
        """
        logging.debug(f"Creating new category with {payload}")
        rq = f"{self.host}/category"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getCategoryByName(self, category_name: str, params: dict = {}):
        """
        Prende categoria da nome.
        """
        logging.debug(f"Find category by name {category_name}")
        rq = f"{self.host}/category/findByName"
        payload = {**params, **{"name": category_name}}
        agent = self.s.getAgent()
        r = agent.get(rq, params=payload)
        return self.s.response(r)

    def updateCategoryCover(self, hub_id: int, category_id: int, localFile):
        """
        Aggiorna cover categoria.
        """
        logging.debug(f"Update hub {hub_id} category {category_id} cover {localFile}")
        rq = f"{self.host}/hub/{hub_id}/category/{category_id}/cover"
        fin = open(localFile, "rb")
        files = {"src": fin}
        agent = self.s.getAgent()
        r = agent.post(rq, files=files)
        return self.s.response(r)

    # catalog
    def listCatalog(self, params: dict = {}):
        """Get catalog by ID"""
        logging.debug(f"List catalogs {params}")
        rq = f"{self.host}/catalog"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getCatalog(self, catalog_id: int, params: dict = {}):
        """Get catalog by ID"""
        logging.debug(f"Get catalog {catalog_id} with params {params}")
        rq = f"{self.host}/catalog/{catalog_id}"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getCatalogHierarchy(self, catalog_id: int, params: dict = {}):
        """Get catalog hiearchy"""
        logging.debug(f"Get catalog {catalog_id} hierarchy with params {params}")
        rq = f"{self.host}/catalog/{catalog_id}/hierarchy"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def createChapter(self, catalog_id: int, payload: dict):
        """Create new catalog chapter."""
        logging.debug(f"Creating new catalog {catalog_id} chapter {payload}")
        rq = f"{self.host}/catalog/{catalog_id}/chapter"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getChapter(self, catalog_id: int, chapter_id: int, params: dict = {}):
        """Get catalog chapter by ID"""
        logging.debug(f"Get catalog chapter {catalog_id}")
        rq = f"{self.host}/catalog/{catalog_id}/chapter/{chapter_id}"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getChapterByName(self, catalog_id: int, name: str, params: dict = {}):
        """Get catalog chapter by NAME"""
        logging.debug(f"Get catalog chapter {name}")
        rq = f"{self.host}/catalog/{catalog_id}/chapter/findByName"
        query = {**params, **{"name": name}}
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def getChapterLeaves(self, catalog_id: int, chapter_id: int, params: dict = {}):
        """Get catalog chapter leaves"""
        logging.debug(f"Get catalog chapter {chapter_id} into catalog {catalog_id}")
        rq = f"{self.host}/catalog/{catalog_id}/chapter/{chapter_id}/leaf"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def createLeaf(self, catalog_id: int, chapter_id: int, payload: dict):
        """Create new catalog chapter leaf."""
        logging.debug(
            f"Creating new catalog {catalog_id} chapter {chapter_id} leaf {payload}"
        )
        rq = f"{self.host}/catalog/{catalog_id}/chapter/{chapter_id}/leaf"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getChapterLeaf(
        self, catalog_id: int, chapter_id: int, leaf_id: int, params: dict = {}
    ):
        """Get catalog chapter leaf ID"""
        logging.debug(f"Get catalog chapter {catalog_id}")
        rq = f"{self.host}/catalog/{catalog_id}/chapter/{chapter_id}/leaf/{leaf_id}"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getChapterLeafByFamilyCode(
        self, catalog_id: int, chapter_id: int, code: str, params: dict = {}
    ):
        """Get catalog chapter leaf by family code."""
        logging.debug(f"Get catalog chapter {chapter_id} leaf by family code {code}")
        rq = f"{self.host}/catalog/{catalog_id}/chapter/{chapter_id}/leaf/findByFamilyCode"
        query = {**params, **{"code": code}}
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def getLeafItems(
        self, catalog_id: int, chapter_id: int, leaf_id: int, params: dict = {}
    ):
        """Get catalog chapter leaves"""
        logging.debug(
            f"Get catalog {catalog_id} chapter {chapter_id} leaf {leaf_id} items"
        )
        rq = (
            f"{self.host}/catalog/{catalog_id}/chapter/{chapter_id}/leaf/{leaf_id}/item"
        )
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def attachLeafItems(
        self, catalog_id: int, chapter_id: int, leaf_id: int, payload: dict
    ):
        """attach leaf items."""
        logging.debug(
            f"Attach items {payload} to catalog {catalog_id} chapter {chapter_id} leaf {leaf_id}"
        )
        rq = (
            f"{self.host}/catalog/{catalog_id}/chapter/{chapter_id}/leaf/{leaf_id}/item"
        )
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    # crimptable
    def createCrimptable(self, payload: dict):
        """Create new crimping table."""
        logging.debug(f"Creating new crtable {payload}")
        rq = f"{self.host}/crimp/table"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getCrimptable(self, table_id: int, params: dict = {}):
        """
        Read crimping table.
        """
        logging.debug(f"Reading crimping table {table_id}")
        rq = f"{self.host}/crimp/table/{table_id}"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getCrimptableFromName(self, name: str, params: dict = {}):
        """
        Read crimping table from name.
        """
        logging.debug(f"Reading crimping table name {name}")
        rq = f"{self.host}/crimp/table/findByName"
        query = {**params, **{"name": name}}
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def getCrimptableFromSlug(self, slug: str, params: dict = {}):
        """
        Read crimping table from slug.
        """
        logging.debug(f"Reading crimping table slug {slug}")
        rq = f"{self.host}/crimp/table/findBySlug"
        query = {**params, **{"slug": slug}}
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def updateCrimptable(self, table_id: int, payload: dict):
        """
        Update crimping table.
        """
        logging.debug(f"Updating crimping table {table_id} with {payload}")
        rq = f"{self.host}/crimp/table/{table_id}"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def patchCrimptable(self, table_id: int, payload: dict):
        """
        Patch crimp table.
        """
        logging.debug(f"Patching table {table_id} with {payload}")
        rq = f"{self.host}/crimp/table/{table_id}"
        agent = self.s.getAgent()
        r = agent.patch(rq, json=payload)
        return self.s.response(r)

    def getCrimptables(self, params: dict = {}):
        """Get crimping tables"""
        logging.debug(f"List crimptable {params}")
        rq = f"{self.host}/crimp/table"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    # crimptable documents
    def addCrimptableDocument(self, table_id: int, localFile, payload: dict):
        """
        Add doc file to Crimp table.
        """
        logging.debug(f"Add {localFile} with {payload} to {table_id}")
        rq = f"{self.host}/crimp/table/{table_id}/doc"
        fin = open(localFile, "rb")
        files = {"src": fin}
        agent = self.s.getAgent()
        r = agent.post(rq, files=files, data=payload)
        return self.s.response(r)

    def removeCrimptableDocument(self, table_id: int, document_id: int):
        """
        Remove doc file to Crimp table.
        """
        logging.debug(f"Removing doc#{document_id} to {table_id}")
        rq = f"{self.host}/crimp/table/{table_id}/doc/{document_id}"
        agent = self.s.getAgent()
        r = agent.delete(rq)
        return self.s.response(r)

    # crimptable matrices
    def createCrimptableMatrix(self, table_id: int, payload: dict):
        """Create new crimping table."""
        logging.debug(f"Creating new crtable matrix {payload}")
        rq = f"{self.host}/crimp/table/{table_id}/matrix"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getCrimptableMatrix(self, table_id: int, matrix_id: int, params: dict = {}):
        """
        Read crimping table matrix.
        """
        logging.debug(f"Reading crimping table {table_id}")
        rq = f"{self.host}/crimp/table/{table_id}/matrix/{matrix_id}"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def updateCrimptableMatrix(self, table_id: int, matrix_id: int, payload: dict):
        """
        Update crimping table matrix.
        """
        logging.debug(
            f"Updating crimping table {table_id} matrix {matrix_id} with {payload}"
        )
        rq = f"{self.host}/crimp/table/{table_id}/matrix/{matrix_id}"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getCrimptableMatrices(self, table_id: int, params: dict = {}):
        """Get crimping table matrices"""
        logging.debug(f"List crimptable {table_id} matrices {params}")
        rq = f"{self.host}/crimp/table/{table_id}/matrix"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    # DEPRECATED VALUES
    # crimptable values

    def createCrimptableValue(self, table_id: int, payload: dict):
        """Create new crimping table."""
        logging.debug(f"Creating new crtable {payload}")
        rq = f"{self.host}/crimp/table/{table_id}/value"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getCrimptableValue(self, table_id: int, value_id: int, params: dict = {}):
        """
        Read crimping table value.
        """
        logging.debug(f"Reading crimping table {table_id}")
        rq = f"{self.host}/crimp/table/{table_id}/value/{value_id}"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def updateCrimptableValue(self, table_id: int, value_id: int, payload: dict):
        """
        Update crimping table value.
        """
        logging.debug(
            f"Updating crimping table {table_id} value {value_id} with {payload}"
        )
        rq = f"{self.host}/crimp/table/{table_id}/value/{value_id}"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getCrimptableValues(self, table_id: int, params: dict = {}):
        """Get crimping tables"""
        logging.debug(f"List crimptable {table_id} values {params}")
        rq = f"{self.host}/crimp/table/{table_id}/value"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    # crimpstyle

    def createCrimpstyle(self, payload: dict):
        """Create new crimping style."""
        logging.debug(f"Creating new crstyle {payload}")
        rq = f"{self.host}/crimp/style"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getCrimpstyle(self, style_id: int, params: dict = {}):
        """
        Read crimping style.
        """
        logging.debug(f"Reading crimping style {style_id}")
        rq = f"{self.host}/crimp/style/{style_id}"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def updateCrimpstyle(self, style_id: int, payload: dict):
        """
        Update crimping style.
        """
        logging.debug(f"Updating crimping style {style_id} with {payload}")
        rq = f"{self.host}/crimp/style/{style_id}"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getCrimpstyles(self, params: dict = {}):
        """Get crimping styles"""
        logging.debug(f"List crimpstyle {params}")
        rq = f"{self.host}/crimp/style"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getCrimpstyleFromName(self, name: str, params: dict = {}):
        """
        Read crimping style from name.
        """
        logging.debug(f"Reading crimping style name {name}")
        rq = f"{self.host}/crimp/style/findByName"
        query = {**params, **{"name": name}}
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    # standardbody
    def createStandardbody(self, payload: dict):
        """Create new standardbody."""
        logging.debug(f"Creating new standardbody {payload}")
        rq = f"{self.host}/standardbody"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getStandardbody(self, stdbody_id: int, params: dict = {}):
        """
        Read standardbody style.
        """
        logging.debug(f"Reading standardbody {stdbody_id}")
        rq = f"{self.host}/standardbody/{stdbody_id}"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getStandardbodyFromName(self, name: str, params: dict = {}):
        """
        Read Standardbody by name.
        """
        logging.info(f"Get standardbody by name {name}")
        query = {**params, **{"name": name}}
        rq = f"{self.host}/standardbody/findByName"
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def patchStandardbody(self, stdbody_id: int, payload: dict):
        """
        Patch standardbody.
        """
        logging.debug(f"Patching standardbody {stdbody_id} with {payload}")
        rq = f"{self.host}/standardbody/{stdbody_id}"
        agent = self.s.getAgent()
        r = agent.patch(rq, json=payload)
        return self.s.response(r)

    # norm
    def createNorm(self, payload: dict):
        """Create new norm."""
        logging.debug(f"Creating norm {payload}")
        rq = f"{self.host}/norm"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getNormFromName(self, name: str, params: dict = {}):
        """
        Prende la norm dal nome.
        """
        logging.info(f"Get norm by name {name}")
        query = {**params, **{"name": name}}
        rq = f"{self.host}/norm/findByName"
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def getNorm(self, norm_id: int, params: dict = {}):
        """
        Read norm style.
        """
        logging.debug(f"Reading norm {norm_id}")
        rq = f"{self.host}/norm/{norm_id}"
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def updateNorm(self, norm_id: int, payload: dict):
        """
        Update norm.
        """
        logging.debug(f"Updating norm {norm_id} with {payload}")
        rq = f"{self.host}/norm/{norm_id}"
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def patchNorm(self, norm_id: int, payload: dict):
        """
        Patch norm.
        """
        logging.debug(f"Patching norm {norm_id} with {payload}")
        rq = f"{self.host}/norm/{norm_id}"
        agent = self.s.getAgent()
        r = agent.patch(rq, json=payload)
        return self.s.response(r)

    # CAD 3D MODEL
    def createCad(self, item_id: int, file: str):
        """create new cad file."""
        logging.debug(f"Creating cad for item {item_id}")
        rq = f"{self.host}/cad"
        payload = {"item_id": item_id}
        files = {"src": open(file, "rb")}
        agent = self.s.getAgent()
        r = agent.post(rq, data=payload, files=files)
        return self.s.response(r)
