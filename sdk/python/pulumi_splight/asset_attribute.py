# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AssetAttributeArgs', 'AssetAttribute']

@pulumi.input_type
class AssetAttributeArgs:
    def __init__(__self__, *,
                 asset: pulumi.Input[str],
                 type: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 unit: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AssetAttribute resource.
        :param pulumi.Input[str] asset: reference to the asset to be linked to
        :param pulumi.Input[str] type: [string|boolean|number] type of the data to be ingested in this attribute
        :param pulumi.Input[str] name: name of the resource
        :param pulumi.Input[str] unit: optional reference to the unit of the measure
        """
        pulumi.set(__self__, "asset", asset)
        pulumi.set(__self__, "type", type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if unit is not None:
            pulumi.set(__self__, "unit", unit)

    @property
    @pulumi.getter
    def asset(self) -> pulumi.Input[str]:
        """
        reference to the asset to be linked to
        """
        return pulumi.get(self, "asset")

    @asset.setter
    def asset(self, value: pulumi.Input[str]):
        pulumi.set(self, "asset", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        [string|boolean|number] type of the data to be ingested in this attribute
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        name of the resource
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[str]]:
        """
        optional reference to the unit of the measure
        """
        return pulumi.get(self, "unit")

    @unit.setter
    def unit(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unit", value)


@pulumi.input_type
class _AssetAttributeState:
    def __init__(__self__, *,
                 asset: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 unit: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AssetAttribute resources.
        :param pulumi.Input[str] asset: reference to the asset to be linked to
        :param pulumi.Input[str] name: name of the resource
        :param pulumi.Input[str] type: [string|boolean|number] type of the data to be ingested in this attribute
        :param pulumi.Input[str] unit: optional reference to the unit of the measure
        """
        if asset is not None:
            pulumi.set(__self__, "asset", asset)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if unit is not None:
            pulumi.set(__self__, "unit", unit)

    @property
    @pulumi.getter
    def asset(self) -> Optional[pulumi.Input[str]]:
        """
        reference to the asset to be linked to
        """
        return pulumi.get(self, "asset")

    @asset.setter
    def asset(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "asset", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        name of the resource
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        [string|boolean|number] type of the data to be ingested in this attribute
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[str]]:
        """
        optional reference to the unit of the measure
        """
        return pulumi.get(self, "unit")

    @unit.setter
    def unit(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unit", value)


class AssetAttribute(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 asset: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 unit: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import pulumi_splight as splight

        asset_test_function_attribute = splight.AssetAttribute("assetTestFunctionAttribute",
            asset="1234-1234-1234-1234",
            type="Number",
            unit="meters")
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        ```sh
        $ pulumi import splight:index/assetAttribute:AssetAttribute [options] splight_asset_attribute.<name> <asset_attribute_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] asset: reference to the asset to be linked to
        :param pulumi.Input[str] name: name of the resource
        :param pulumi.Input[str] type: [string|boolean|number] type of the data to be ingested in this attribute
        :param pulumi.Input[str] unit: optional reference to the unit of the measure
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AssetAttributeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import pulumi_splight as splight

        asset_test_function_attribute = splight.AssetAttribute("assetTestFunctionAttribute",
            asset="1234-1234-1234-1234",
            type="Number",
            unit="meters")
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        ```sh
        $ pulumi import splight:index/assetAttribute:AssetAttribute [options] splight_asset_attribute.<name> <asset_attribute_id>
        ```

        :param str resource_name: The name of the resource.
        :param AssetAttributeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssetAttributeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 asset: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 unit: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AssetAttributeArgs.__new__(AssetAttributeArgs)

            if asset is None and not opts.urn:
                raise TypeError("Missing required property 'asset'")
            __props__.__dict__["asset"] = asset
            __props__.__dict__["name"] = name
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["unit"] = unit
        super(AssetAttribute, __self__).__init__(
            'splight:index/assetAttribute:AssetAttribute',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            asset: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            unit: Optional[pulumi.Input[str]] = None) -> 'AssetAttribute':
        """
        Get an existing AssetAttribute resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] asset: reference to the asset to be linked to
        :param pulumi.Input[str] name: name of the resource
        :param pulumi.Input[str] type: [string|boolean|number] type of the data to be ingested in this attribute
        :param pulumi.Input[str] unit: optional reference to the unit of the measure
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AssetAttributeState.__new__(_AssetAttributeState)

        __props__.__dict__["asset"] = asset
        __props__.__dict__["name"] = name
        __props__.__dict__["type"] = type
        __props__.__dict__["unit"] = unit
        return AssetAttribute(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def asset(self) -> pulumi.Output[str]:
        """
        reference to the asset to be linked to
        """
        return pulumi.get(self, "asset")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        [string|boolean|number] type of the data to be ingested in this attribute
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def unit(self) -> pulumi.Output[Optional[str]]:
        """
        optional reference to the unit of the measure
        """
        return pulumi.get(self, "unit")

